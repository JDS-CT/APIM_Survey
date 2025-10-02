# Problem → Solution Log
- 2025-10-02: `pytest -q --maxfail=1 --cov=.` failed because `pytest-cov` is not installed in the environment. Reran the suite without the coverage flag once tests were configured.
- 2025-10-02: `pip install flask` was blocked by the environment proxy (403). Replaced the Flask dependency with a standard-library HTTP server implementation instead.
