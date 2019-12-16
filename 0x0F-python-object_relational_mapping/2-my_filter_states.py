#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """Lists all states where name matches the argument"""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    arg = argv[4]
    c.execute("SELECT * FROM states "
              "WHERE states.name = %s "
              "ORDER BY states.id ASC", (arg,))
    res = c.fetchall()
    for row in res:
            print(row)
    c.close()
    db.close()
