import sqlite3 as lite
import sys
from tkinter import W

#take first arguments as path
path = sys.argv[1]
conn = lite.connect(path)
cur = conn.cursor()

def get_tables():
    with conn:
        #cur.execute("SELECT * FROM *")
        #select all from all tables
        command = """SELECT name FROM sqlite_master  
  WHERE type='table';"""
        cur.execute(command)
        return cur.fetchall()

init = get_tables()
with conn:
    for table in init:
        command = "SELECT * FROM " + table[0]
        cur.execute(command)
        print(table[0])
        print(cur.fetchall())