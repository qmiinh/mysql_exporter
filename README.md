# MySQL Server Exporter [![Build Status](https://travis-ci.org/prometheus/mysqld_exporter.svg)][travis]

[![CircleCI](https://circleci.com/gh/prometheus/mysqld_exporter/tree/master.svg?style=shield)][circleci]
[![Docker Repository on Quay](https://quay.io/repository/prometheus/mysqld-exporter/status)][quay]
[![Docker Pulls](https://img.shields.io/docker/pulls/prom/mysqld-exporter.svg?maxAge=604800)][hub]
[![Go Report Card](https://goreportcard.com/badge/github.com/prometheus/mysqld_exporter)](https://goreportcard.com/report/github.com/prometheus/mysqld_exporter)

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

You can deploy this exporter using the [prom/mysqld-exporter](https://registry.hub.docker.com/u/prom/mysqld-exporter/) Docker image.

For example:

```bash

docker run -p 4444:4444 <Image name>
