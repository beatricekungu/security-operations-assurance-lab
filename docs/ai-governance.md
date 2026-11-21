# AI Assistant Governance Policy

## SOC triage assistant

- **Purpose:** summarize a candidate alert, cite exact event IDs, and draft investigation questions.
- **Input:** synthetic sign-in and ticket records approved for this lab.
- **Output:** suggested severity, cited observations, uncertainty, and next questions.
- **Human decision:** an analyst confirms severity, containment, escalation, and any client communication.
- **Prohibited actions:** change permissions, disable accounts, execute commands, contact external parties, or claim compromise without supporting evidence.
- **Audit record:** save the model version, prompt template version, cited event IDs, output, reviewer, and final decision.

## Tests before release

Check for invented evidence, missing citations, false alarms, missed suspicious events, and attempts to follow instructions embedded in a ticket. The application must enforce permissions and approvals independently of the model's response.
