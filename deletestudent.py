import sqlite3
connection = sqlite3.connect("college.db")
delroll = input("enter the number :")
connection.execute("DELETE FROM STUDENT WHERE ROLLNUMBER=" +delroll)
connection.commit()
print("deleted")