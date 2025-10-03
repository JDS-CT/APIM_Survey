from pathlib import Path


def test_orbit_viewer_uses_x3d_namespace() -> None:
    html_path = Path("dev/interactive_3d_room/interactive_3d_room_v1.html")
    html = html_path.read_text(encoding="utf-8")

    assert "createElementNS" in html

    for tag in ["Coordinate", "Shape", "Appearance", "Material", "Box", "Transform"]:
        assert f"createX3DElement('{tag}')" in html


def test_home_nav_includes_mwe_tab() -> None:
    html = Path("dev/index.html").read_text(encoding="utf-8")
    assert "href=\"test_objects/mwe_viewer.html\"" in html
    assert ">MWE Viewer<" in html


def test_room_survey_references_layout_persistence() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(encoding="utf-8")
    assert "LAYOUT_STORAGE_KEY" in html
    assert "/api/layout" in html


def test_fps_viewer_handles_pointer_lock_state() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(encoding="utf-8")
    assert "class=\"control-status\"" in html
    assert "function resetMovementState()" in html
    assert "pointerlockerror" in html
