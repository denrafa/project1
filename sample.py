import sqlite3
import sys

db_conn =sqlite3.connect('test.db')
print("database Created")

db_conn.close()
print("database closed")