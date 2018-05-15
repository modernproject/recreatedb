
# import sys
import click
from recreatedb.core import (
    configuration,
    run
)


@click.group()
def cli():
    """recreatedb."""
    # if sys.version_info[0] == 2:
    #     print("Current environment is Python 2.")
    #     print("Please use a Python 3.6 virtualenv.")
    #     raise SystemExit


@cli.command('start')
# @click.option('--path', default='~/all_databases.sql', help='Database Location', required=True)
def start():
    run()


@cli.command('configure')
def configure():
    configuration()


def main():
    cli()

if __name__ == '__main__':
    main()
