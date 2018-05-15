
import json
import sys
import subprocess
import os.path
from shutil import copy2

POSTGRES_APP_DIR = "/Applications/Postgres.app/Contents/Versions/latest/bin/psql"

HOME_DIR = os.path.expanduser('~')
USER_CONFIG = os.path.join(HOME_DIR, '.recreatedb')
RECREATEDB_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
GLOBAL_CONFIG_EMPTY = os.path.join(
    RECREATEDB_DIR, 'recreatedb', 'config', '.recreatedb')


def configuration():
    """Base configuration of recreatedb for current system."""
    copy2(GLOBAL_CONFIG_EMPTY, USER_CONFIG)


def get_config():
    """Retrieve the config data."""
    if not os.path.isfile(USER_CONFIG):
        configuration()
    else:
        config_file = open(USER_CONFIG, "r")
    try:
        config_data = json.load(config_file)
        config_file.close()
        for k, v in config_data.items():
            if not v:
                sys.exit("Missing value for {}".format(k))
        return config_data
    except json.decoder.JSONDecodeError as e:
        print("User configuration has malformed JSON.")
        print(e)
        raise SystemExit


def check_postgres_install():
    """Ensure system has Postgres installed and available on the shell."""
    if POSTGRES_APP_DIR not in \
            subprocess.check_output(['which', 'psql']).decode("utf-8"):
        install_postgres()


def install_postgres(*args, **kwargs):
    """Install Postgres or Postgres App."""
    subprocess.run(['open', 'https://postgresapp.com/'])
    sys.exit('Please install Postgres by navigating to https://postgresapp.com/')


def dropdb(*args, **kwargs):
    """Drop specific database."""
    subprocess.run(['dropdb', kwargs['DATABASE_NAME']])
    print("Dropping database {}".format(kwargs['DATABASE_NAME']))


def createdb(*args, **kwargs):
    """Create an empty database from named argument."""
    subprocess.run(['createdb', kwargs['DATABASE_NAME']])
    print("Creating empty database {}".format(kwargs['DATABASE_NAME']))


def loaddb(*args, **kwargs):
    """Load a database dump into an exisiting or empty database."""
    print("Loading database...")
    cmd = " ".join(['psql', '-d', kwargs['DATABASE_NAME'],
                    '-f', kwargs['DUMP_LOCATION']])
    subprocess.run(cmd, shell=True)


def check_for_dump(*args, **kwargs):
    """Ensure a database dump exists to work with."""
    if not os.path.isfile(kwargs['DUMP_LOCATION']):
        print("No database found at {}".format(kwargs['DUMP_LOCATION']))
        raise SystemExit


def grant_permissions(*args, **kwargs):
    """Grand permissions to db user."""
    subprocess.run(["psql", "-c", "GRANT ALL PRIVILEGES ON database {} TO {}".format(
        kwargs['DATABASE_NAME'], kwargs['DATABASE_USER'])])


def alert_django_user(*args, **kwargs):
    """Ensure Django user can create dbs."""
    subprocess.run(["psql", "-c", "ALTER USER django CREATEDB"])


def run():
    """Run the entire system."""
    config = get_config()

    check_postgres_install()
    check_for_dump(**config)
    dropdb(**config)
    createdb(**config)
    loaddb(**config)
    grant_permissions(**config)
    alert_django_user()
