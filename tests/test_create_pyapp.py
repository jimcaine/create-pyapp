import os
import shutil
from pathlib import Path
from create_pyapp import create_python_app


def test_create_python_app():
    project_name = "unittest_project"
    project_path = Path(os.getcwd()) / project_name
    target_paths = [
        project_path,
        project_path / "pyproject.toml",
        project_path / ".env",
    ]

    create_python_app(project_name, project_path, virtualenv=False)
    for target_path in target_paths:
        assert os.path.exists(target_path)

    shutil.rmtree(project_path)


def test_create_python_app_virtualenv():
    project_name = "unittest_project"
    project_path = Path(os.getcwd()) / project_name
    target_paths = [
        project_path,
        project_path / "pyproject.toml",
        project_path / ".env",
        project_path / ".venv",
    ]

    create_python_app(project_name, project_path, virtualenv=True)
    for target_path in target_paths:
        assert os.path.exists(target_path)

    shutil.rmtree(project_path)


def test_create_python_app_git():
    project_name = "unittest_project"
    project_path = Path(os.getcwd()) / project_name
    target_paths = [
        project_path,
        project_path / "pyproject.toml",
        project_path / ".env",
        project_path / ".git",
    ]

    create_python_app(project_name, project_path, git_init=True)
    for target_path in target_paths:
        assert os.path.exists(target_path)

    shutil.rmtree(project_path)


def test_create_python_app_tmuxinator():
    project_name = "unittest_project"
    project_path = Path(os.getcwd()) / project_name
    target_path = os.path.expanduser(
        f"~/.config/tmuxinator/{project_name}.yml")

    create_python_app(project_name, project_path, tmuxinator=True)
    assert os.path.exists(project_path)
    assert os.path.exists(project_path / "pyproject.toml")
    assert os.path.exists(project_path / ".env")
    assert os.path.exists(target_path)

    shutil.rmtree(project_path)
    os.remove(target_path)
