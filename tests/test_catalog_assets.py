from __future__ import annotations

import json
from pathlib import Path


def test_sample_catalog_lists_new_assets() -> None:
    catalog_path = Path("resources/layout_samples/catalog.json")
    data = json.loads(catalog_path.read_text(encoding="utf-8"))
    assets = data.get("assets", {})

    expected_keys = {
        "thermostat_wall",
        "thermostat_ceiling",
        "chiller",
        "n2_bottle",
        "wall_air_barb",
        "bottled_air_line",
        "table_resizable",
    }

    for key in expected_keys:
        assert key in assets, f"Expected asset {key} in sample catalog"

    thermostat_ceiling = assets["thermostat_ceiling"]
    sockets = thermostat_ceiling.get("connectionSockets", [])
    assert any(sock.get("surface") == "ceiling" for sock in sockets)


def test_default_catalog_script_mentions_new_assets() -> None:
    script = Path("dev/shared/scripts/cable_catalog_defaults.js").read_text(
        encoding="utf-8"
    )
    for key in (
        "thermostat_wall",
        "thermostat_ceiling",
        "chiller",
        "n2_bottle",
        "wall_air_barb",
        "bottled_air_line",
        "table_resizable",
    ):
        assert key in script
