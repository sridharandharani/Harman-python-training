while True:
    print("Select an option from the menu :")
    print("1.Add 2 numbers")
    print("2.subtract 2 numbers")
    print("3.multiply 2 numbers")
    print("4.divide 2 numbers")
    print("5. EXIT")

    choice = int(input("Enter the choice :"))
    if choice == 1:
        x = int(input("Enter 1st number :"))
        y = int(input("Enter 2nd number :"))
        z = x + y
        print(z)
    elif choice == 2:
        x = int(input("Enter 1st number :"))
        y = int(input("Enter 2nd number :"))
        z = x - y
        print(z)

    elif choice == 3:
        x = int(input("Enter 1st number :"))
        y = int(input("Enter 2nd number :"))
        z = x * y
        print(z)

    elif choice == 4:
        x = int(input("Enter 1st number :"))
        y = int(input("Enter 2nd number :"))
        z = x / y
        print(z)

    elif choice == 5:
        break
    else:
        print("Invalid choice")


#  wtp to stop the information about a mobile phone using menu
#  id brand model name serial num manufacturing year month price
# add
#
# search using serial
# view all
# update using serial
# delete using serial
# database mobile.db
# table smartphones