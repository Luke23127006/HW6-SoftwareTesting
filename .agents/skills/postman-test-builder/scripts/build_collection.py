from pathlib import Path
import json
import yaml

ROOT = Path.cwd()

API_FOLDERS = {
    "login": "Pool A - Login",
    "apply-coupon": "Pool B - Apply Coupon",
    "admin-create-coupon": "Pool C - Admin Create Coupon",
}

def load_tests(folder):
    path = ROOT / "tests" / folder / "final-tests.yaml"
    if not path.exists():
        return []
    return yaml.safe_load(path.read_text(encoding="utf-8")) or []

def assertion_script(test):
    test_id = test["id"]
    expected = test.get("expected") or {}
    status = expected.get("status")
    assertions = expected.get("assertions") or []

    lines = [
        f'pm.test("{test_id} - response exists", function () {{',
        "  pm.expect(pm.response).to.exist;",
        "});",
    ]

    if isinstance(status, int):
        lines += [
            f'pm.test("{test_id} - status code", function () {{',
            f"  pm.response.to.have.status({status});",
            "});",
        ]

    for index, assertion in enumerate(assertions, start=1):
        label = str(assertion).replace('"', "'")
        lines += [
            f'pm.test("{test_id} - assertion {index}: {label}", function () {{',
            "  // TODO: replace with a precise executable assertion.",
            "  pm.expect(true).to.eql(true);",
            "});",
        ]

    return lines

def build_item(test):
    request = test["request"]
    path = request["path"]

    headers = [
        {"key": str(k), "value": str(v)}
        for k, v in (request.get("headers") or {}).items()
    ]

    body = request.get("body")

    if body is not None and not any(
        h.get("key", "").lower() == "content-type"
        for h in headers
    ):
        headers.append({
            "key": "Content-Type",
            "value": "application/json"
        })

    item = {
        "name": f'{test["id"]} | {test["title"]}',
        "request": {
            "method": request["method"],
            "header": headers,
            "url": {
                "raw": "{{baseUrl}}" + path,
                "host": ["{{baseUrl}}"],
                "path": [
                    segment
                    for segment in path.strip("/").split("/")
                    if segment
                ],
            },
        },
        "event": [{
            "listen": "test",
            "script": {
                "type": "text/javascript",
                "exec": assertion_script(test),
            },
        }],
    }

    if body is not None:
        item["request"]["body"] = {
            "mode": "raw",
            "raw": json.dumps(body, ensure_ascii=False),
            "options": {"raw": {"language": "json"}},
        }

    return item

def main():
    config_path = ROOT / "config" / "hw06.yaml"
    if not config_path.exists():
        raise SystemExit("Run this script from the HW6 repository root.")

    config = yaml.safe_load(
        config_path.read_text(encoding="utf-8")
    )

    collection = {
        "info": {
            "name": "HW06 API Testing",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        },
        "event": [{
            "listen": "prerequest",
            "script": {
                "type": "text/javascript",
                "exec": [
                    "pm.request.headers.upsert({",
                    '  key: "X-Student-Id",',
                    '  value: pm.environment.get("studentId")',
                    "});",
                ],
            },
        }],
        "item": [
            {
                "name": display,
                "item": [build_item(test) for test in load_tests(folder)]
            }
            for folder, display in API_FOLDERS.items()
        ],
    }

    postman_dir = ROOT / "postman"
    postman_dir.mkdir(parents=True, exist_ok=True)

    (postman_dir / "HW06.postman_collection.json").write_text(
        json.dumps(collection, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    environment = {
        "name": "HW06 Local",
        "values": [
            {
                "key": "baseUrl",
                "value": config["sut"]["base_url"],
                "enabled": True,
            },
            {
                "key": "studentId",
                "value": str(config["student"]["id"]),
                "enabled": True,
            },
            {"key": "userToken", "value": "", "enabled": True},
            {"key": "adminToken", "value": "", "enabled": True},
        ],
    }

    (postman_dir / "local.postman_environment.json").write_text(
        json.dumps(environment, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print("Postman collection and environment generated.")
    print("IMPORTANT: replace placeholder pm.expect(true) assertions before final execution.")

if __name__ == "__main__":
    main()
