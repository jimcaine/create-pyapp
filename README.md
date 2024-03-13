# create-pyapp
Utilities for quickly bootstrapping new python packages.

The below command will create a new directory in the current working directory and do the following:
1. Create a new README.md file with your project name.
2. Create pyproject.toml file with your project name and some defaults.
3. Create .gitignore file with some defaults.
4. Create a new python virtual environment in the project directory .venv.
5. Active this virtual environment.
6. If tmuxinator is true, a new tmuxinator yaml file will be created in ~/.config/tmuxinator to easily bootstrap a new tmux environment.

```bash
create-pyapp my-app --tmuxinator true
```

The project directory layout will look like the following
```text
./my-app
├── .venv
├── README.md
├── project_name
│   ├── __init__.py
├── pyproject.toml
├── tests
│   └── unit
│       ├── __init__.py

~/.config
├── tmuxinator
│   └── my-app.yml
```
