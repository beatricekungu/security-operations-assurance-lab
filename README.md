# Security Operations & Assurance Lab

A portfolio project for a fictional organization connecting IAM, SOC detection, DFIR, recovery, GRC evidence, and governed AI assistants. This repository starts with a small, reproducible privileged sign-in detection.

## First release

The synthetic sign-in data contains normal events, suspicious events, and a legitimate travel event that requires analyst review. A deterministic Python rule flags successful privileged sign-ins from an unexpected country or an unmanaged device. An alert is a review candidate, not a finding of compromise.

Run with Python 3.10 or newer. No cloud service, API key, or third-party Python package is required.

```powershell
python -m detections.privileged_signin data/synthetic/signins.csv
python -m unittest discover -s tests -v
```

On Windows, `py` may work instead of `python`. See [the scenario](docs/scenario.md), [AI governance policy](docs/ai-governance.md), and [analyst review](docs/analyst-review.md).

## Ten connected releases

1. Asset inventory and risk register
2. IAM roles and access review
3. Sign-in and application log pipeline
4. SOC detection rules
5. Alert triage and AI assistant
6. DFIR evidence and timeline
7. Containment and recovery exercise
8. Cloud and CI/CD configuration checks
9. Continuous GRC control evidence
10. Executive incident and risk view

## Evidence standard

Each release will include source data, code or configuration, expected and observed results, analyst reasoning, and a documented fix or decision. All data is fictional. Run attack exercises only in this isolated lab or systems with explicit authorization. Never commit credentials, real client data, or destructive malware.

