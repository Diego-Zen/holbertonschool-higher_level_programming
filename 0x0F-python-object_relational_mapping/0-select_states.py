#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """Lists all states"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    res = c.fetchall()
    for row in res:
            print(row)
    c.close()
    db.close()
