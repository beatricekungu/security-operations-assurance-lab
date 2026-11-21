"""Flag privileged sign-ins that need analyst review.

This rule deliberately makes no claim that an alert proves compromise.
"""

import argparse
import csv
import json
from pathlib import Path


REQUIRED_COLUMNS = {
    "event_id", "timestamp", "user", "role", "app", "result",
    "observed_country", "usual_country", "device_managed",
}
PRIVILEGED_ROLES = {"admin", "security_admin"}


def detect(events):
    """Return review candidates with their source event and exact reasons."""
    alerts = []
    for event in events:
        missing = REQUIRED_COLUMNS.difference(event)
        if missing:
            raise ValueError(f"Event missing columns: {', '.join(sorted(missing))}")

        if event["result"].strip().lower() != "success":
            continue
        if event["role"].strip().lower() not in PRIVILEGED_ROLES:
            continue

        reasons = []
        if event["observed_country"].strip().upper() != event["usual_country"].strip().upper():
            reasons.append("country differs from account baseline")
        if event["device_managed"].strip().lower() == "false":
            reasons.append("device is unmanaged")

        if reasons:
            alerts.append({
                "event_id": event["event_id"],
                "user": event["user"],
                "app": event["app"],
                "timestamp": event["timestamp"],
                "reasons": reasons,
                "status": "needs analyst review",
            })
    return alerts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Synthetic sign-in CSV")
    args = parser.parse_args()
    with args.csv_path.open(encoding="utf-8", newline="") as source:
        events = list(csv.DictReader(source))
    print(json.dumps(detect(events), indent=2))


if __name__ == "__main__":
    main()
