from pathlib import Path
import subprocess
import logging

logger = logging.getLogger(__name__)


def initialize_git(project_path: Path) -> None:
    """Initialize a git repository.

    :param project_path: The path to the project directory.
    """
    logger.info(f"Initializing git repository in {project_path}")
    result = subprocess.run(
        ["git", "init", str(project_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to initialize git: {result.stderr}")
