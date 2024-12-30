from .ProjectFileScope import ProjectFileScope

from pathlib import Path
from importlib import resources
from typing import Dict, Any
import jinja2
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class ProjectFile:
    """A project file to be created.

    The ProjectFile object describes a file and how to create it. It contains
    the scope of the file, the path to the template, the relative path to the
    project directory, and the parameters to be used when creating the file.

    :param scope: The scope of the file.
    :param template_path: The path to the template file.
    :param relative_path: The relative path to the project directory.
    :param params: The parameters to be used when creating the file.
    """
    scope: ProjectFileScope
    template_path: str
    relative_path: str
    params: Dict[str, Any]

    def __setattr__(self, name, value):
        if name == 'scope':
            assert isinstance(value, ProjectFileScope), \
                "scope must be a ProjectFileScope"
        self.__dict__[name] = value

    @property
    def template(self) -> jinja2.Template:
        """Read a template from the resources.

        :return: The contents of the template.
        """
        resource_path = resources.files(self.scope.module_path)
        file_path = resource_path / (self.template_path)
        text = file_path.read_text()
        return jinja2.Template(text)

    def write_template(self, project_path: Path | None = None) -> None:
        """Write a template from the resources.

        :param project_path: The path to the project directory.
        :return: The contents of the template.
        """
        if project_path is None:
            file_path = Path(self.scope.target_path) / self.relative_path
        else:
            file_path = project_path / self.relative_path

        logger.info("Rendering template")
        rendered = self.template.render(**self.params)

        logger.info(f"Creating directory: {file_path.parent}")
        file_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Writing file: {file_path}")
        with open(file_path, "w") as f:
            f.write(rendered)
