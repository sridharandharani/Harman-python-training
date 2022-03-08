import sqlite3

connection = sqlite3.connect("college.db") #create a db

# connection.execute(''' CREATE TABLE STUDENT(
#                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                         NAME TEXT,
#                         ROLLNUMBER INTEGER,
#                         ADMNO INTEGER,
#                         COLLEGE TEXT
#
# ); ''') #table created

print("table created")


getname = input("Enter the name :")
getrollnumber = input("Enter the roll number :")
getadmno = input("Enter the admno :")
getcollege = input("Enter the college name :")

connection.execute(" INSERT INTO STUDENT(NAME,ROLLNUMBER,ADMNO,COLLEGE) \
VALUES('"+getname+"',"+getrollnumber+","+getadmno+",'"+getcollege+"')")   #inserting values
connection.commit()
connection.close()
print("inserted sucessfully")