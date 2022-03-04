#wtp to read information of book name, author name ,price ,publisher name
library = []
count = int(input("enter the number of books to be read :"))
for i in range (0,count):
    book_name = input("Enter the book name:")
    author_name = input("Enter the author name :")
    price = int(input("Enter the price :"))
    publisher_name = input("Enter the publisher name :")
    mylib = {"bookname" : book_name , "authorname" : author_name , "price" : price , "publisher name": publisher_name}
    library.append(mylib)
    print((library))