# APIM Survey Prototype Workspace

This workspace hosts the microscope room planning prototypes that move from 2D
layout capture to 3D review. Everything you need to run the current iteration
lives under `dev/`, and the landing page links to the four supported flows:

* **Home** (`dev/index.html`) &mdash; overview and navigation hub.
* **2D Survey** (`dev/room_survey_min/room_survey_min_v1.html`) &mdash; capture room
  dimensions, equipment, sockets, walls, and doors.
* **Orbit Viewer** (`dev/interactive_3d_room/interactive_3d_room_v1.html`) &mdash;
  extrude the survey export and orbit the room.
* **First-Person Demo**
  (`dev/interactive_3d_room/interactive_3d_room_fps_demo.html`) &mdash; walk the
  space with WASD controls and place sample 3D assets.

Older experiments now live in `dev/archive/` to keep the navigation focused.

## Running the prototype server

The Python standard-library server in `dev/server.py` serves the entire `dev/`
directory and persists layouts to disk. From the repository root:

```bash
python dev/server.py
```

You should see output similar to:

```
Serving prototypes on http://127.0.0.1:5000/ (layout store: dev/data/saved_layout.json)
```

Open that URL in a browser to access the landing page and linked prototypes. The
server exposes a simple JSON API at `/api/layout` that the Orbit Viewer uses to
save and restore layouts (`GET` returns the last saved payload, `POST` persists
the provided JSON object).

## 2D &rarr; 3D workflow

1. Launch the 2D Survey from the home page, adjust the room and equipment, and
   click **Export JSON**. The browser downloads `room_survey.json`.
2. Visit the Orbit Viewer, click **Import Layout**, and choose that JSON file.
   Successful imports flash a green status banner and refresh the 3D scene.
3. (Optional) Visit the First-Person Demo, click **Import 2D Layout JSON**, and
   pick the same export to update the walkthrough and collision bounds.
4. Use **Save Layout** in the Orbit Viewer to write the current snapshot to the
   server (persisted at `dev/data/saved_layout.json`).

If you need a known-good file for testing, `resources/layout_samples/default_room.json`
matches the default survey preset.
