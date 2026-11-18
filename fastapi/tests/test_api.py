"""在独立进程中使用 TestClient 验证各项目。"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
CLIENT_SCRIPT = """
import json
import sys

from fastapi.testclient import TestClient
from main import app

method, path, body = json.loads(sys.argv[1])
with TestClient(app) as client:
    response = client.request(method, path, json=body)
    content_type = response.headers.get('content-type', '')
    payload = response.json() if 'application/json' in content_type else response.text
    print(json.dumps([response.status_code, payload]))
"""


def request(project: str, method: str, path: str, body: dict | None = None) -> list:
    result = subprocess.run(
        [sys.executable, "-c", CLIENT_SCRIPT, json.dumps([method, path, body])],
        cwd=EXAMPLES / project,
        capture_output=True,
        encoding="utf-8",
        check=True,
        timeout=20,
    )
    return json.loads(result.stdout)


CASES = json.loads(r"""
[
  [
    "01-hello-world",
    "GET",
    "/",
    null,
    200,
    {
      "message": "你好，FastAPI"
    }
  ],
  [
    "01-hello-world",
    "GET",
    "/health",
    null,
    200,
    {
      "status": "ok"
    }
  ],
  [
    "02-routing",
    "GET",
    "/users/1?verbose=true",
    null,
    200,
    {
      "id": 1,
      "name": "小林"
    }
  ],
  [
    "02-routing",
    "GET",
    "/users?limit=1",
    null,
    200,
    [
      {
        "id": 1,
        "name": "小林"
      }
    ]
  ],
  [
    "02-routing",
    "POST",
    "/users",
    {
      "name": "小陈"
    },
    201,
    {
      "id": 3,
      "name": "小陈"
    }
  ],
  [
    "02-routing",
    "GET",
    "/users/99",
    null,
    404,
    {
      "detail": "用户不存在"
    }
  ],
  [
    "02-routing",
    "GET",
    "/products",
    null,
    200,
    [
      {
        "name": "笔记本"
      }
    ]
  ],
  [
    "03-pydantic",
    "POST",
    "/profiles",
    {
      "name": " 小林 ",
      "age": 20,
      "address": {
        "city": "上海"
      }
    },
    200,
    {
      "name": "小林",
      "age": 20,
      "nickname": null,
      "address": {
        "city": "上海"
      },
      "tags": []
    }
  ],
  [
    "03-pydantic",
    "POST",
    "/profiles",
    {
      "name": "小林",
      "age": 17,
      "address": {
        "city": "上海"
      }
    },
    422,
    null
  ],
  [
    "02-routing",
    "GET",
    "/users/nope",
    null,
    422,
    null
  ],
  [
    "02-routing",
    "GET",
    "/users?limit=0",
    null,
    422,
    null
  ],
  [
    "02-routing",
    "POST",
    "/users",
    {},
    422,
    null
  ]
]
""")


@pytest.mark.parametrize(("project", "method", "path", "body", "status", "expected"), CASES)
def test_api(project, method, path, body, status, expected):
    actual_status, payload = request(project, method, path, body)
    assert actual_status == status
    if expected is None:
        assert payload["detail"]
        assert payload["detail"][0]["loc"][0] in {"body", "path", "query"}
    else:
        assert payload == expected


@pytest.mark.parametrize("project", ["01-hello-world", "02-routing", "03-pydantic"])
def test_documentation(project):
    for route, marker in [("/docs", "Swagger UI"), ("/redoc", "ReDoc")]:
        status, text = request(project, "GET", route)
        assert status == 200
        assert marker.lower() in text.lower()
    status, schema = request(project, "GET", "/openapi.json")
    assert status == 200
    assert schema["paths"]
