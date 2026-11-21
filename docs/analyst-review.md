# First Detection Review

Run `python -m detections.privileged_signin data/synthetic/signins.csv`.

| Event | Why flagged | Analyst disposition |
| --- | --- | --- |
| E004 | Privileged successful login on an unmanaged device | Investigate device ownership and recent account activity |
| E007 | Privileged successful login from a country outside the account baseline | Candidate false positive; verify travel or approved remote access |
| E010 | Privileged successful login from a country outside the account baseline | High-priority investigation; correlate with MFA and session activity |

The rule is intentionally narrow. It does not detect password spraying, impossible travel, or data exfiltration yet. A country difference alone is insufficient to establish compromise.
