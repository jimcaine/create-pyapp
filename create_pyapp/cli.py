import click
from pathlib import Path
from .create_pyapp import create_python_app

params = {
    'project_path': {
        'type': Path,
        'required': False,
        'help': 'The path to create the project',
    },
    'tmuxinator': {
        'type': bool,
        'default': False,
        'help': 'Create a tmuxinator file',
    }
}



@click.command()
@click.argument('project_name', type=str)
@click.option('--project-path', **params['project_path'])
@click.option('--tmuxinator', **params['tmuxinator'])
def main(
    project_name: str,
    project_path: str | None,
    tmuxinator: bool,
):
    """Create a Python project"""
    if project_path:
        project_path_ = Path(project_path) / project_name
    else:
        project_path_ = Path.cwd() / project_name
    click.echo(f'Project path: {project_path_}')

    create_python_app(project_name, project_path_, tmuxinator=tmuxinator)
