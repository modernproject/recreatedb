import click
from recreatedb.core import configuration

@click.group()
def cli():
    """recreatedb
    """
    # if sys.version_info[0] == 2:
    #     print("Current environment is Python 2.")
    #     print("Please use a Python 3.6 virtualenv.")
    #     raise SystemExit

@cli.command(None)
def run(user, cli):
    configuration()

@cli.command('configure')
def configure(user, cli):
    configuration()


def main():
    cli()


if __name__ == '__main__':
    main()
