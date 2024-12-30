from enum import Enum
import os


class ProjectFileScope(Enum):
    """ The scope name of a file created for the project.

    The ProjectFileScope is used to determine the resource path to the scope
    directory and the target path to the scope directory. It is bound to the
    ProjectFile class to determine where to find the templates and where to
    write the files when building the project.


    :PROJECT: The project scope - files that are created in the project
        directory.
    :TMUXINATOR: The tmuxinator scope - files that are created in the tmuxinator
        configuration directory. This is typically `~/.config/tmuxinator` on a
        Unix system.

    :property module_path: The resource path to the scope directory. This is
        where to find the templates when building the project.
    :property target_path: The target path to the scope directory. This is where
        to write the files when building the project.
    """
    PROJECT = "PROJECT"
    TMUXINATOR = "TMUXINATOR"

    @property
    def module_path(self) -> str:
        """Get the resource path to the scope directory.

        :return: The path to the scope directory.
        """
        scope_map = {
            self.PROJECT: 'crappy.assets.project',
            self.TMUXINATOR: 'crappy.assets.tmuxinator',
        }

        return scope_map[self]

    @property
    def target_path(self) -> str:
        """Get the target path to the scope directory.

        :return: The path to the scope directory.
        """
        scope_map = {
            self.TMUXINATOR: os.path.expanduser('~/.config/tmuxinator'),
        }

        return scope_map[self]
