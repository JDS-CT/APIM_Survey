# Problem → Solution Log
- 2025-10-02: `pytest -q --maxfail=1 --cov=.` failed because `pytest-cov` is not installed in the environment. Reran the suite without the coverage flag once tests were configured.
- 2025-10-02: `pip install flask` was blocked by the environment proxy (403). Replaced the Flask dependency with a standard-library HTTP server implementation instead.
- 2025-10-03: `pytest -q --maxfail=1 --cov=.` still fails because the `pytest-cov` plugin is not installed in the environment. Reran the suite without the coverage flag.
- 2025-10-03: `black --check .` flagged `tests/test_frontend_markup.py` formatting drift. Ran `black tests/test_frontend_markup.py` to restore compliance before rerunning the check.
- 2025-10-05: `pnpm test --run --reporter=dot`, `pnpm lint`, and `pnpm typecheck` failed because no package manifest is present at the repository root. Skipped pnpm-based checks since this prototype does not ship a Node workspace.
