#!/usr/bin/python3
"""Lists all states where name matches the argument free of sql injections"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name LIKE BINARY %s ORDER BY states.id ASC""", (argv[4],))
    query_res = cur.fetchall()
    for row in query_res:
            print("{}".format(row))
    cur.close()
    conn.close()
