from pathlib import Path
import subprocess
import logging

logger = logging.getLogger(__name__)


def initialize_git(project_path: Path) -> None:
    """Initialize a git repository.

    :param project_path: The path to the project directory.
    """
    logger.info(f"Initializing git repository in {project_path}")
    command = ["git", "init", str(project_path)]
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        diagnostics = result.stderr.strip() or result.stdout.strip() or "No output captured."
        raise RuntimeError(
            f"Failed to initialize git with command {' '.join(command)!r} "
            f"(exit code {result.returncode}): {diagnostics}"
        )
