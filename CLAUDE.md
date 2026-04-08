# mplplots

Visual styling helpers for Matplotlib/Seaborn.

## Environment

- Python >=3.12, use the `.venv` virtual environment: `source .venv/bin/activate`
- Install: `pip install -e ".[dev]"`

## Commands

- **Test**: `pytest` (runs from `tests/`, verbose+stdout by default)
- **Single test**: `pytest tests/test_utils.py::TestAutoTicks::test_sets_ticks_on_simple_plot`
- **Lint**: `ruff check src/ tests/`
- **Format**: `ruff format src/ tests/`
- **Type check**: `mypy src/`
- **Pre-commit**: `pre-commit run --all-files`

## Code Style

- Ruff for linting and formatting (line length 100, Google-style docstrings)
- Mypy for type checking (strict-ish, see pyproject.toml)
- `src/` layout with `mplplots` package
- Tests in `tests/` using pytest (no docstrings required in tests)
- Type annotations on all public functions
