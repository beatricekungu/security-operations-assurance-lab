# Fictional Company and First Scenario

Harborlight Services is a fictional mid-sized company with a ticketing app, a cloud administration console, and an identity provider. Its SOC reviews sign-in activity for privileged users. All names and records in this lab are invented.

## Question

Which successful privileged sign-ins require investigation, and what evidence would justify containment?

## First data set

The CSV contains twelve events. E004 uses an unmanaged device; E007 is a managed-device login from another country; E010 is a privileged login from another country. E007 is intentionally a candidate false positive: the analyst should verify an approved travel record or contact the account owner before deciding whether it is malicious.

## Next step

Join these events to synthetic IAM permissions, application activity, and analyst decisions. Later releases will add a contained attack exercise and verified remediation.
