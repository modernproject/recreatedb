
def configuration():
    """
    Base configuration of recreatedb for current system.
    """
    pass

def check_postgres_install():
    """
    Ensure system has Postgres installed and available on the shell.
    """
    pass
    if (false):
        install_postgres()

def install_postgres():
    """
    Install Postgres or Postgres App.
    """
    pass

def dropdb():
    """
    Drop specific database.
    """
    pass

def createdb():
    """
    Create an empty database from named argument.
    """
    pass

def loaddb():
    """
    Loads a database dump into an exisiting or empty database.
    """
    pass

def check_for_dump();
    """
    Ensure a database dump exists to work with.
    """
    pass

def create_dump():
    """
    Create a dump of the current database.
    """
    pass

def run():
    check_postgres_install()
    check_for_dump()
    dropdb()
    createdb()
    loaddb()
