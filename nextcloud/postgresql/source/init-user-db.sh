#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
    CREATE USER nextcloud WITH PASSWORD 'nextcloud';
    CREATE DATABASE nextcloud;
    GRANT ALL PRIVILEGES ON DATABASE nextcloud TO nextcloud;
EOSQL