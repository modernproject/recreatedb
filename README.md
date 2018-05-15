# recreatedb

## Useful for Testing Postgres Databases for Django Deployments

Command Line Interface tool that looks for a database backup in the form of an .sql file, removes a local Postgres database, recreates it, then adds the database data to the newly created one.

To use it assumes you have the Postgres command line tools available on your bash config/profile. If you do not have these tools follow the _Install Postgres App_ section.

## Install recreatedb

To add `recreatedb` to the your path, clone it then run the following to create a simlink.

```bash
# Commands
pip3 install recreatedb
```

## Configure

```bash
# Commands
recreatedb configure
```

This will create a JSON configuration file at `~/.recreatedb`:

```
{
  "DATABASE_NAME": "<databse>",
  "DATABASE_USER": "<user>",
  "DUMP_LOCATION": "<location of SQL file>"
}
```

Please update this with your supplied data.

## Usage

To use `recreatedb` please ensure you have installed Postgres, have updated the `.recreatedb` configuration file, and have a SQL file readily available you wish to load.

```bash
# Commands
recreatedb start
```

## Install Postgres App

This is a GUI interface for PostgreSQL databases. Find it here: https://postgresapp.com/

Post installation it is important to add Postgres's tools to your system path. Based on the official docs run the following:

```bash
# Command
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

Use which psql to confirm installation while in the virtualenv.

## Development

*   To create edits please branch and clone the repository.
*   Cd into the directory and install + activate a new Pipenv.
*   To package use setup.py upload
