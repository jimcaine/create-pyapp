from pathlib import Path
import subprocess
import logging

logger = logging.getLogger(__name__)


def create_virtualenv(project_path: Path) -> Path:
    """Create virual environment `.venv` in project directory.

    :param project_path: The path to the project directory.
    :return: The path to the virtual environment binary.
    """
    venv_path = project_path / ".venv"
    logger.info(f"Creating virtual environment in {venv_path}")
    result = subprocess.run(
        ["uv", "venv", str(venv_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to create virtual environment: {result.stderr}")
    return venv_path / "bin" / "python"
