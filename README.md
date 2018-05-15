# recreatedb

## Useful for Testing Postgres Databases for Django Deployments

Command Line Interface tool that looks for a database backup in the form of an .sql file, removes a local Postgres database, recreates it, then adds the database data to the newly created one.

To use it assumes you have the Postgres command line tools available on your bash config/profile. If you do not have these tools follow the _Install Postgres App_ section.

## Install Postgres App

This is a GUI interface for PostgreSQL databases. Find it here: https://postgresapp.com/

Post installation it is important to add Postgres's tools to your system path. Based on the official docs run the following:

```bash
# Command
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

Use which psql to confirm installation while in the virtualenv.

## Install recreatedb

To add `recreatedb` to the your path, clone it then run the following to create a simlink.

```bash
# Commands
git clone git@github.com:djstein/bentobox-recreatedb.git

sudo ln -s <path to bentbox-recreatedb>/bin/recreatedb /usr/local/bin/recratedb
# Example Simlink
sudo ln -s ~/git/bentobox-recreatedb/bin/recreatedb /usr/local/bin/recreatedb
```

## Usage

To use `recreatedb` either supply an argument to an .sql backup or if no input is used it will look for `~/Downloads/all_databases.sql`

```bash
# Commands
recreatedb

recreatedb all_databases.sql

recreatedb /foo/bar.sql
```

_NOTE:_ Currently only takes full absolute paths

## Development

*   To create edits please branch and clone the repository.
*   Cd into the directory and install + activate a new Pipenv.
*   To package use setup.py upload
