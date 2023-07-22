# TimescaleDB
## Configuration
### timescaledb
- network:
    ```bash
    docker network create --attachable --driver bridge timescale_network
    ```
- docker-compose.timescaledb.yml
    1. It uses the `timescale_network` created in the previous step.
    2. It uses a volume to persist the database’s data, even if the Docker container is removed or replaced. This is very common for `Dockerized` databases.
    3. It uses port `5432` (this will be important when we try to access the database in the future).
    4. It uses a custom configuration file, and a `.env` file to store secret database connection information, like your database password.
- postgresql configuration file: `postgresql_custom.conf`
- `.env` file

### pgadmin
- docker-compose.pgadmin.yml

## Running the timescaledb
```bash
docker-compose -f docker-compose.timescale.yml -p timescaledb up -d
```

## Running pgadmin
- Bring up the service:
    ```bash
    docker-compose -f docker-compose.pgadmin.yml -p pgadmin up -d
    ```
- Resolving the possible port conflict
    1. find the pid using the port:
        ```bash
        lsof -i:9000
        ```
    2. kill the process `[pid]`:
        ```bash
        kill [pid]
        ```
- Accessing the service: http://localhost:9000