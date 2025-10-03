"""Lightweight HTTP server for the room survey prototypes.

Environment variables
---------------------
``APIM_SURVEY_LAYOUT_STORE``
    Optional absolute or relative path that overrides the layout persistence
    location. Relative values are resolved against the current working
    directory.

The module emits informational logs via the ``apim_survey.server`` logger for
startup, shutdown, and layout persistence events to aid troubleshooting.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler
import socketserver
from pathlib import Path
from typing import Any, Tuple

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_STORE_PATH = BASE_DIR / "data" / "saved_layout.json"
ENV_STORE_PATH = "APIM_SURVEY_LAYOUT_STORE"


LOGGER = logging.getLogger("apim_survey.server")


def resolve_store_path(store_override: Path | None = None) -> Path:
    """Resolve the effective layout store path with env and CLI overrides."""

    if store_override is not None:
        candidate = Path(store_override)
    else:
        env_value = os.getenv(ENV_STORE_PATH)
        candidate = Path(env_value) if env_value else DEFAULT_STORE_PATH

    candidate = candidate.expanduser()
    if not candidate.is_absolute():
        candidate = (Path.cwd() / candidate).resolve()
    else:
        candidate = candidate.resolve()
    return candidate


class LayoutStore:
    """Persist layout JSON to a file on disk."""

    def __init__(self, path: Path) -> None:
        self.path = path
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            LOGGER.error(
                "Failed to prepare layout store directory %s: %s", self.path.parent, exc
            )

    def read(self) -> Any:
        if not self.path.exists():
            return None
        try:
            raw = self.path.read_text(encoding="utf-8")
        except OSError as exc:
            LOGGER.warning("Unable to read layout store %s: %s", self.path, exc)
            return None
        if not raw.strip():
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            LOGGER.error("Failed to parse layout store %s: %s", self.path, exc)
            return None

    def write(self, payload: dict[str, Any]) -> None:
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            LOGGER.error(
                "Unable to create layout store directory %s: %s", self.path.parent, exc
            )
            raise
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        LOGGER.info("Layout saved to %s", self.path)


class LayoutRequestHandler(SimpleHTTPRequestHandler):
    """Serve static prototype assets and a small JSON API."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A003
        LOGGER.debug("HTTP %s", format % args)

    def _json_response(self, payload: Any, status: HTTPStatus = HTTPStatus.OK) -> None:
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _store(self) -> LayoutStore:
        return self.server.layout_store  # type: ignore[attr-defined]

    def do_GET(self) -> None:  # noqa: N802
        if self.path.rstrip("?") == "/api/layout":
            payload = {"layout": self._store().read()}
            self._json_response(payload)
            LOGGER.info("Served layout read request")
            return
        super().do_GET()

    def do_POST(self) -> None:  # noqa: N802
        if self.path.rstrip("?") != "/api/layout":
            self.send_error(HTTPStatus.NOT_FOUND, "Not Found")
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            self._json_response({"error": "Invalid JSON body."}, HTTPStatus.BAD_REQUEST)
            LOGGER.warning("Rejected layout save with invalid JSON")
            return

        if not isinstance(payload, dict):
            self._json_response(
                {"error": "Expected JSON object."}, HTTPStatus.BAD_REQUEST
            )
            LOGGER.warning("Rejected layout save with non-object payload")
            return

        self._store().write(payload)
        self._json_response({"status": "saved"})
        LOGGER.info("Processed layout save request")


class LayoutHTTPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(
        self,
        server_address: Tuple[str, int],
        handler: type[LayoutRequestHandler],
        store_path: Path,
    ) -> None:
        normalized_store = resolve_store_path(store_path)
        super().__init__(server_address, handler)
        self.layout_store = LayoutStore(normalized_store)
        self.store_path = normalized_store


def run_server(
    host: str = "127.0.0.1", port: int = 5000, store_path: Path | None = None
) -> None:
    """Run the threaded HTTP server until interrupted."""
    store = resolve_store_path(store_path)
    LOGGER.info("Starting server on %s:%s with store %s", host, port, store)
    with LayoutHTTPServer((host, port), LayoutRequestHandler, store) as httpd:
        print(f"Serving prototypes on http://{host}:{port}/ (layout store: {store})")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server...")
            LOGGER.info("Shutdown requested by user")
            httpd.shutdown()
    LOGGER.info("Server stopped")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve the room survey prototypes with persistence."
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host/IP to bind")
    parser.add_argument("--port", type=int, default=5000, help="Port to listen on")
    parser.add_argument(
        "--store",
        type=Path,
        default=DEFAULT_STORE_PATH,
        help="Path to the JSON file used to persist layouts",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    run_server(host=args.host, port=args.port, store_path=args.store)
