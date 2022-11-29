from os import name
import sqlite3

con=sqlite3.connect("sample.db")
print("database created....")

con.execute("create table sudha(name TEXT,email TEXT,address TEXT)");

print("table created...")