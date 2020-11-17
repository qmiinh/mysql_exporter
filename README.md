# MySQL Server Exporter [![Build Status](https://travis-ci.org/prometheus/mysqld_exporter.svg)][travis]

[![Docker Pulls](https://img.shields.io/docker/pulls/prom/mysqld-exporter.svg?maxAge=604800)][hub]


Prometheus exporter for MySQL server metrics.

Supported versions:
* MySQL >= 5.6.
* MariaDB >= 10.1

NOTE: Not all collection methods are supported on MySQL/MariaDB < 5.6

## Building and running

### Required Grants

```sql
CREATE USER 'exporter'@'localhost' IDENTIFIED BY 'XXXXXXXX' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'localhost';
```

## Using Docker

For example:

```bash

docker run -p 4444:4444 <Image name>
