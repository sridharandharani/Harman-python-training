import sqlite3
connection = sqlite3.connect("college.db")

result = connection.execute("SELECT * FROM STUDENT ")
for i in result:
    print("Id :",i[0])
    print("Name :",i[1])
    print("Rollnumber :",i[2])
    print("Admno :", i[3])
    print("College :",i[4])

