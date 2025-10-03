from pathlib import Path


def test_orbit_viewer_uses_x3d_namespace() -> None:
    html_path = Path("dev/interactive_3d_room/interactive_3d_room_v1.html")
    html = html_path.read_text(encoding="utf-8")

    assert "createElementNS" in html

    for tag in ["Coordinate", "Shape", "Appearance", "Material", "Box", "Transform"]:
        assert f"createX3DElement('{tag}')" in html
