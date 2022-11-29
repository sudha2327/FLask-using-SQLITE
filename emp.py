from os import name
import sqlite3


con=sqlite3.connect("database.db")
print("Database created successfully")

con.execute("create table employee2(name TEXT,email TEXT,address TEXT)");

print("table created...")

con.execute("INSERT INTO employee2 (name,email,address)  values('sudha','h@gmail.com','hii')")
print("inserted successfully")
con.commit()

cursor=con.execute("SELECT name,email,address from employee2");

for row in cursor:
    print("name==",row[0])
    print("email==",row[1])
    print("address==",row[2])

print("operation successfully")

con.close()
