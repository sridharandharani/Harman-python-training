#create a menu
while True:
    print("Select an option from menu :")
    print("1. Add an employee")
    print("2. search an employee")
    print("3. update an employee")
    print("4. delete an employee")
    print("5. EXIT")

    choice = int(input("Enter the choice :"))
    if choice == 1:
        print("Selected an option to enter an employee details")

    elif choice == 2:
        print("Selected an option to search an employee details")

    elif choice == 3:
        print("Selected an option to update an employee details")

    elif choice == 4:
        print("Selected an option to delete an employee details")

    elif choice == 5:
        break

    else:
        print("Invalid choice")
