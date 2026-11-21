import csv
import unittest
from pathlib import Path

from detections.privileged_signin import detect


DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic" / "signins.csv"


class PrivilegedSigninTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with DATA.open(encoding="utf-8", newline="") as source:
            cls.events = list(csv.DictReader(source))

    def test_expected_review_candidates(self):
        self.assertEqual(
            [alert["event_id"] for alert in detect(self.events)],
            ["E004", "E007", "E010"],
        )

    def test_failed_signin_and_nonprivileged_signin_are_not_flagged(self):
        alerts = detect(self.events)
        event_ids = {alert["event_id"] for alert in alerts}
        self.assertNotIn("E003", event_ids)
        self.assertNotIn("E011", event_ids)

    def test_alerts_include_source_and_reason(self):
        alert = next(a for a in detect(self.events) if a["event_id"] == "E004")
        self.assertEqual(alert["reasons"], ["device is unmanaged"])
        self.assertEqual(alert["status"], "needs analyst review")


if __name__ == "__main__":
    unittest.main()
