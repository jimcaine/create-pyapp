from .ProjectFileScope import ProjectFileScope
from .ProjectFile import ProjectFile
from ._virtenv import create_virtualenv
from ._git import initialize_git

from pathlib import Path
import logging
logger = logging.getLogger(__name__)


def create_python_app(
    project_name: str,
    project_path: Path,
    git_init: bool = True,
    virtualenv: bool = True,
    tmuxinator: bool = False,
    github_actions: bool = False,
) -> None:
    """Bootstrap a new Python project.

    :param project_name: The name of the project.
    :param project_path: The path to the project directory.
    :param git_init: Initialize a git repository.
    :param virtualenv: Create a virtual environment.
    :param tmuxinator: Create a tmuxinator configuration file.
    """
    project_path.mkdir(parents=True, exist_ok=True)

    src_path = project_path / project_name
    src_path.mkdir(parents=True, exist_ok=True)
    init_file = src_path / "__init__.py"
    init_file.touch()

    project_files = [
        ProjectFile(
            scope=ProjectFileScope.PROJECT,
            template_path="pyproject.toml.jinja",
            relative_path="pyproject.toml",
            params={"project_name": project_name},
        ),
        ProjectFile(
            scope=ProjectFileScope.PROJECT,
            template_path=".env.jinja",
            relative_path=".env",
            params={},
        ),
        ProjectFile(
            scope=ProjectFileScope.PROJECT,
            template_path="README.md.jinja",
            relative_path="README.md",
            params={"project_name": project_name},
        ),
        ProjectFile(
            scope=ProjectFileScope.PROJECT,
            template_path=".gitignore.jinja",
            relative_path=".gitignore",
            params={},
        ),
        ProjectFile(
            scope=ProjectFileScope.PROJECT,
            template_path="Makefile.jinja",
            relative_path="Makefile",
            params={},
        ),
        ProjectFile(
            scope=ProjectFileScope.PROJECT,
            template_path="tests/__init__.py.jinja",
            relative_path="tests/__init__.py",
            params={},
        ),
    ]

    if github_actions:
        project_files.append(
            ProjectFile(
                scope=ProjectFileScope.PROJECT,
                template_path=".github/workflows/main-pr.yml.jinja",
                relative_path=".github/workflows/main-pr.yml",
                params={},
            )
        )

    for file in project_files:
        logger.info(f"Writing file: {file}")
        file.write_template(project_path)

    if tmuxinator:
        ProjectFile(
            scope=ProjectFileScope.TMUXINATOR,
            template_path="tmuxinator-cfg.yml.jinja",
            relative_path=f"{project_name}.yml",
            params={
                "project_name": project_name,
                "project_path": project_path,
            },
        ).write_template()

    if virtualenv:
        python_binary = create_virtualenv(project_path)
        logger.info(f"Created virtual environment: {python_binary}")
        logger.info(
            f"Install dependencies: {python_binary} -m pip install -r requirements.txt")

    if git_init:
        initialize_git(project_path)
        logger.info(f"Initialized git repository: {project_path}")
        logger.info(f"Add files to git: cd {project_path} && git add .")


__all__ = ['create_python_app']
