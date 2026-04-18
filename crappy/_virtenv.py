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
    cmd = ["uv", "venv", str(venv_path)]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        details = stderr or stdout
        if stderr and stdout:
            details = f"{stderr}\n{stdout}"
        raise RuntimeError(
            f"Failed to create virtual environment with command {cmd!r} "
            f"(return code {result.returncode})"
            f"{': ' + details if details else ''}"
        )
    return venv_path / "bin" / "python"
