# crappy
Command line interface for quickly bootstrapping new python packages.

This project is highly opinionated and is designed as a personal tool to quickly bootstrap new projects to my liking.

## Installation
```bash
pip install git+https://www.github.com/jimcaine/create-pyapp
```

## Usage
```bash
crappy my-app --tmuxinator --gha
```

The project directory layout will look like the following
```text
./my-app/
├── .env
├── .github/
│   ├── workflows/
│       ├── pr-main.yml
├── .git/
├── .venv/
├── README.md
├── project_name/
│   ├── __init__.py
├── pyproject.toml
├── tests/
│   └── unit/
│       ├── __init__.py

~/.config/
├── tmuxinator/
│   └── my-app.yml
```
