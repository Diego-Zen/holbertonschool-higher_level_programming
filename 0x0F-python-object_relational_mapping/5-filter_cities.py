#!/usr/bin/python3
"""Lists all cities by state where state name matches the argument
free of sql injections"""
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
    cur.execute("""SELECT c.name
    FROM cities AS c
    INNER JOIN states AS s ON s.id = c.state_id
    WHERE s.name LIKE BINARY %s
    ORDER BY c.id ASC""", (argv[4],))
    query_res = cur.fetchall()
    new_list = []
    for row in query_res:
        for col in row:
            new_list.append(col)
    print(*new_list, sep=', ')
    cur.close()
    conn.close()
