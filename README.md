# APIM Survey Prototype Workspace

This repository now groups the survey and room-planning experiments into a
`dev/` workspace so new iterations can be spun up without overwriting earlier
work. The structure is designed to support a "pick the best of three" flow for
key pages.

```
dev/
├── interactive_3d_room/
│   └── interactive_3d_room_v1.html    # X3DOM-driven 3D preview baseline
├── room_survey_min/
│   ├── room_survey_min_v1.html        # Baseline grid & drag prototype
│   ├── room_survey_min_v2.html        # Copy ready for next experiment
│   └── room_survey_min_v3.html        # Alternate copy for experimentation
├── shared/
│   └── styles/
│       └── portal_overview.css        # Dark/neon portal theme
└── x3d_inline_with_2ft_cube/
    └── x3d_inline_with_2ft_cube_v1.html
```

The `3d_resources/` directory is kept at the repository root so the assets can
be fed into both the 2D editor and any 3D preview that needs to inline them.
Each HTML page currently references assets relative to its own folder, making it
straightforward to duplicate a version directory when branching experiments.

To start a new iteration on `room_survey_min`, clone the baseline version that
performed best, increment the version suffix, and begin editing.
