# crappy 🐍

A CLI tool for bootstrapping new Python projects with opinionated defaults — batteries included, no bikeshedding.

> Designed as a personal tool. Highly opinionated by design.

## Installation

```bash
pip install git+https://www.github.com/jimcaine/create-pyapp
```

## Usage

```bash
crappy <project-name> [OPTIONS]
```

### Options

| Flag | Description |
|------|-------------|
| `--project-path PATH` | Where to create the project (defaults to current directory) |
| `--tmuxinator` | Generate a [tmuxinator](https://github.com/tmuxinator/tmuxinator) config |
| `--gha` | Add a GitHub Actions CI workflow |

### Examples

Scaffold a basic project in the current directory:

```bash
crappy my-app
```

Scaffold with GitHub Actions and a tmuxinator config:

```bash
crappy my-app --gha --tmuxinator
```

Scaffold into a specific directory:

```bash
crappy my-app --project-path ~/projects
```

## What gets generated 📁

```text
my-app/
├── .env
├── .gitignore
├── .git/
├── .venv/
├── Makefile
├── README.md
├── my_app/
│   └── __init__.py
├── pyproject.toml
└── tests/
    └── __init__.py
```

With `--gha`:

```text
my-app/
└── .github/
    └── workflows/
        └── main-pr.yml
```

With `--tmuxinator`:

```text
~/.config/tmuxinator/
└── my-app.yml
```

## What's included ✨

- **`pyproject.toml`** — pre-configured with `pydantic` and `pandas`, ready for `uv` or `pip`
- **`Makefile`** — targets for `test`, `pr`, `pr-dev`, and `increment-patch-version`
- **`.env`** — placeholder for environment variables
- **`.gitignore`** — sensible Python defaults
- **GitHub Actions** *(optional)* — PR workflow targeting `main`
- **tmuxinator** *(optional)* — session config written to `~/.config/tmuxinator/`
- **`uv venv`** — virtual environment created automatically
- **`git init`** — repo initialized out of the box
