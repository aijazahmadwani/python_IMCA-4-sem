import sqlite3
db_file="company.db"
conn=sqlite3.connect(db_file)
#table name COMPANY
data=conn.execute("SELECT * FROM COMPANY")
#conn.commit()
#print(data)
for d in data:
    print(d)
