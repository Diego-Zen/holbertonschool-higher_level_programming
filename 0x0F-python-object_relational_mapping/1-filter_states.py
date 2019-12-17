#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """Lists all states with name starting with N"""
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
    WHERE ASCII(name) = 78
    ORDER BY states.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
            print(row)
    cur.close()
    conn.close()
