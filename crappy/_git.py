from pathlib import Path
import os
import logging

logger = logging.getLogger(__name__)


def initialize_git(project_path: Path) -> None:
    """Initialize a git repository.

    :param project_path: The path to the project directory.
    """
    logger.info(f"Initializing git repository in {project_path}")
    os.system(f"git init {project_path}")
