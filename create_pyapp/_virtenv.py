from pathlib import Path
import os
import logging

logger = logging.getLogger(__name__)


def create_virtualenv(project_path: Path) -> Path:
    """Create virual environment `.venv` in project directory.

    :param project_path: The path to the project directory.
    :return: The path to the virtual environment binary.
    """
    venv_path = project_path / ".venv"
    logger.info(f"Creating virtual environment in {venv_path}")
    os.system(f"python -m venv {venv_path}")
    return venv_path / "bin" / "python"
