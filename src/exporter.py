#!/usr/bin/env python
import pymysql, prometheus_client
import threading, os
import socket
import time
from prometheus_client import Gauge,CollectorRegistry,start_http_server

#PORT_NUMBER
port_expose=os.getenv('port_expose')

def gather_data(registry):

    # Get the host name of the machine
    host = socket.gethostname()

    # Create our collectors
    mysql_seconds_behind_master = Gauge(
            "mysql_slave_seconds_behind_master",
            "MySQL slave secons behind master",
            ["host", "method"],
            )
    mysql_io_running = Gauge(
            "mysql_slave_io_running",
            "MySQL slave IO Running",
            ["host", "method"],
            )
    mysql_sql_running = Gauge(
            "mysql_slave_sql_running",
            "MySQL slave SQL Running",
            ["host", "method"],
            )

    # register the metric collectors
    registry.register(mysql_seconds_behind_master)
    registry.register(mysql_io_running)
    registry.register(mysql_sql_running)

    # connect to db
    host=os.getenv('host_db')
    port=os.getenv('port_db')
    user=os.getenv('user_db')
    password=os.getenv('pass_db')

    connection = pymysql.connect(host=str(host), user=str(user), password=str(password), port=int(port))
    cur = connection.cursor(pymysql.cursors.DictCursor)

    while True:
        time.sleep(1)
    # Get replication infomation
        cur.execute('show slave status')
        #connection.close()
        slave_status = cur.fetchone()
        slave_file = slave_status["Seconds_Behind_Master"]
        slave_sql_running = 1 if slave_status["Slave_SQL_Running"] == "Yes" else 0
        slave_io_running = 1 if slave_status["Slave_IO_Running"] == "Yes" else 0

    #Add metrics
        mysql_seconds_behind_master.labels(host, "mysql_seconds_behind_master").set(slave_file)
        mysql_io_running.labels(host, "mysql_io_running").set(slave_io_running)
        mysql_sql_running.labels(host, "mysql_sql_running").set(slave_sql_running)


if __name__ == "__main__":
    # Create the registry
    registry = CollectorRegistry()
    thread = threading.Thread(target=gather_data, args=(registry, ))
    thread.start()
    # Set a server to export (expose to prometheus) the data (in a thread)
    try:
        # We make this to set the registry in the handler
        start_http_server(int(port_expose))

    except KeyboardInterrupt:
        server.socket.close()
        thread.join()

