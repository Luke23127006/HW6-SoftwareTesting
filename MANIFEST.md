# HW06 Skill Support Files

Extract this ZIP directly into the HW6 repository root.

It adds only the missing support resources under:

```text
.agents/skills/<skill>/scripts/
.agents/skills/<skill>/references/
.agents/skills/<skill>/assets/
```

It does not overwrite any `SKILL.md`.

After extraction:

```bash
python -m pip install -r requirements.txt
```

Then create the runtime workspace folders if they do not exist:

```powershell
mkdir tests\login
mkdir tests\apply-coupon
mkdir tests\admin-create-coupon
mkdir postman\data
mkdir reports\newman
mkdir evidence
mkdir bugs
mkdir ai-logs
mkdir docs\report-sections
```
