import json
import sys
import threading
import time
from http.client import HTTPConnection
from pathlib import Path
from typing import Generator, Tuple, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dev.server import LayoutHTTPServer, LayoutRequestHandler, LayoutStore  # noqa: E402


@pytest.fixture
def layout_store(tmp_path: Path) -> LayoutStore:
    return LayoutStore(tmp_path / "layout.json")


def test_store_round_trip(layout_store: LayoutStore) -> None:
    assert layout_store.read() is None
    payload = {"room": {"W": 7200, "L": 5400}, "floor_items": []}
    layout_store.write(payload)
    assert layout_store.read() == payload


@pytest.fixture
def running_server(
    tmp_path: Path,
) -> Generator[Tuple[str, int, LayoutHTTPServer], None, None]:
    server = LayoutHTTPServer(
        ("127.0.0.1", 0), LayoutRequestHandler, tmp_path / "layout.json"
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    # Small delay to ensure the server is ready before issuing requests.
    time.sleep(0.05)
    address = cast(Tuple[str, int], server.server_address)
    host, port = address
    try:
        yield host, port, server
    finally:
        server.shutdown()
        thread.join(timeout=1)


def test_http_api_round_trip(running_server) -> None:
    host, port, server = running_server
    conn = HTTPConnection(host, port, timeout=2)

    conn.request("GET", "/api/layout")
    response = conn.getresponse()
    assert response.status == 200
    data = json.loads(response.read().decode("utf-8"))
    assert data == {"layout": None}

    layout_payload = {
        "room": {"W": 6400, "L": 8200},
        "triangle": {"x": 1200, "y": 1800},
    }
    conn.request(
        "POST",
        "/api/layout",
        body=json.dumps(layout_payload),
        headers={"Content-Type": "application/json"},
    )
    post_response = conn.getresponse()
    assert post_response.status == 200
    assert json.loads(post_response.read().decode("utf-8")) == {"status": "saved"}

    conn.request("GET", "/api/layout")
    second_get = conn.getresponse()
    assert second_get.status == 200
    assert json.loads(second_get.read().decode("utf-8")) == {"layout": layout_payload}

    conn.request(
        "POST",
        "/api/layout",
        body=json.dumps([1, 2, 3]),
        headers={"Content-Type": "application/json"},
    )
    invalid_response = conn.getresponse()
    assert invalid_response.status == 400
    assert "error" in json.loads(invalid_response.read().decode("utf-8"))

    conn.close()
