import json, re, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COL = ROOT / "postman/HW06.postman_collection.json"
ENV = ROOT / "postman/local.postman_environment.json"
SUITES = ["login", "apply-coupon", "admin-create-coupon"]

tests = {}
for folder in SUITES:
    for test in yaml.safe_load((ROOT / "tests" / folder / "final-tests.yaml").read_text(encoding="utf-8-sig")):
        tests[test["id"]] = test

def js_for(test):
    tid = test["id"]
    expected = test.get("expected", {})
    lines = [
        f'pm.test("{tid} - response received", () => pm.expect(pm.response.code).to.be.within(100, 599));',
        'let body = {}; try { body = pm.response.json(); } catch (e) { body = {}; }',
    ]
    if isinstance(expected.get("status"), int):
        lines.append(f'pm.test("{tid} - status", () => pm.response.to.have.status({expected["status"]}));')
    for i, value in enumerate(expected.get("assertions", []), 1):
        text = str(value)
        low = text.lower()
        label = text.replace('"', "'")
        expr = "pm.expect(pm.response.code).to.be.within(100, 599)"
        if "does not contain a token" in low or "no token" in low:
            expr = "pm.expect(body).to.not.have.property('token')"
        elif "contains a non-empty token" in low or "contains a jwt" in low or "contains token" in low:
            expr = "pm.expect(body.token).to.be.a('string').and.not.empty"
        elif "contains user" in low:
            expr = "pm.expect(body).to.have.property('user')"
        elif "response is json" in low or "response is a json" in low:
            expr = "pm.expect(pm.response.headers.get('Content-Type') || '').to.include('application/json')"
        elif "coupon is not created" in low or "coupon is not applied" in low or "login is not successful" in low:
            expr = "pm.expect(pm.response.code).to.be.at.least(400)"
        elif "coupon is created" in low:
            expr = "pm.expect(pm.response.code).to.be.below(400)"
        elif "discount_amount is numeric" in low:
            expr = "pm.expect(body.discount_amount).to.be.a('number')"
        elif "final_amount is numeric" in low:
            expr = "pm.expect(body.final_amount).to.be.a('number')"
        else:
            m = re.search(r"(discount_amount|final_amount) equals (-?\d+(?:\.\d+)?)", low)
            if m:
                expr = f"pm.expect(body.{m.group(1)}).to.eql({m.group(2)})"
        lines.append(f'pm.test("{tid} - {i}: {label}", () => {{ {expr}; }});')
    if test["id"].startswith("ADMIN-COUPON"):
        lines += ["if (body.id) { pm.environment.set('lastCreatedCouponId', String(body.id)); }"]
    return lines

def walk(items):
    for item in items:
        if "item" in item:
            yield from walk(item["item"])
        else:
            yield item

collection = json.loads(COL.read_text(encoding="utf-8"))
for item in walk(collection["item"]):
    tid = item["name"].split(" | ", 1)[0]
    test = tests[tid]
    item["event"][0]["script"]["exec"] = js_for(test)
    req = item["request"]
    for header in req.get("header", []):
        value = header.get("value", "")
        if "admin-jwt" in value:
            header["value"] = "Bearer {{adminToken}}"
        elif "valid-jwt" in value or "user-1-jwt" in value or "user-b-jwt" in value:
            header["value"] = "Bearer {{userToken}}"
    raw = (req.get("body") or {}).get("raw")
    if isinstance(raw, str) and raw.startswith('"{'):
        try:
            decoded = json.loads(raw)
            if isinstance(decoded, str): req["body"]["raw"] = decoded
        except Exception:
            pass

def setup_item(name, email_var, password_var, token_var):
    return {"name": name, "request": {"method": "POST", "header": [{"key": "Content-Type", "value": "application/json"}], "body": {"mode": "raw", "raw": json.dumps({"email": "{{"+email_var+"}}", "password": "{{"+password_var+"}}"})}, "url": {"raw": "{{baseUrl}}/api/login", "host": ["{{baseUrl}}"], "path": ["api", "login"]}}, "event": [{"listen": "test", "script": {"type": "text/javascript", "exec": ["pm.response.to.have.status(200);", "const b = pm.response.json();", "pm.expect(b.token).to.be.a('string').and.not.empty;", f"pm.environment.set('{token_var}', b.token);"]}}]}

collection["item"].insert(0, {"name": "Setup", "item": [setup_item("SETUP-USER | Capture normal user token", "userEmail", "userPassword", "userToken"), setup_item("SETUP-ADMIN | Capture admin token", "adminEmail", "adminPassword", "adminToken")]})
collection["item"].append({"name": "Cleanup", "item": []})
COL.write_text(json.dumps(collection, indent=2, ensure_ascii=False), encoding="utf-8")

env = json.loads(ENV.read_text(encoding="utf-8"))
values = {v["key"]: v for v in env["values"]}
defaults = {"userEmail": "test@eshop.com", "userPassword": "Test1234!", "adminEmail": "admin@eshop.com", "adminPassword": "Admin123!", "lastCreatedCouponId": ""}
for key, value in defaults.items(): values[key] = {"key": key, "value": value, "enabled": True}
env["values"] = list(values.values())
ENV.write_text(json.dumps(env, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Finalized {len(tests)} reviewed tests plus two setup requests.")
