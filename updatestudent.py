import sqlite3
connection = sqlite3.connect("college.db")
getroll = input("Enter the roll number ?")

getname = input("Enter the name :")
getadmno = input("Enter the admno :")
getcollege = input("Enter the college :")
connection.execute("UPDATE STUDENT SET \
NAME='"+getname+"',ADMNO= "+getadmno+",COLLEGE= '"+getcollege+"'\
 WHERE ROLLNUMBER = " +getroll)
connection.commit()
print("updated sucessfully")

result = connection.execute("SELECT * FROM STUDENT ")
for i in result:
    print("Id :",i[0])
    print("Name :",i[1])
    print("Rollnumber :",i[2])
    print("Admno :", i[3])
    print("College :",i[4])