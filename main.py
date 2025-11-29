print("----WELCOME TO THE PHONEBOOK MANAGER.----")

choices = ['1.Add Contact', '2.View Contacts', '3.Search Contact', '4.Delete Contact', '5.Exit']

print(choices)

phonebook = {}

while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input; please enter a number between 1 and 5.")
        continue

    if choice == 1:
        while True:
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            phonebook[name] = number
            more = input("Add another contact? (y/n): ")
            if more.lower() != 'y':
                break
        print("Contact/s added successfully.")

    elif choice == 2:
        if len(phonebook) > 0:
            for name, number in phonebook.items():
                print(f"Name: {name}, Number: {number}")
        else:
            print("No contacts found.")

    elif choice == 3:
        search_name = input("Enter the name to search: ")
        if search_name in phonebook:
            print(f"Found: Name: {search_name}, Number: {phonebook[search_name]}")
        else:
            print("Contact not found.")

    elif choice == 4:
        del_name = input("Enter the name to delete: ")
        if del_name in phonebook:
            del phonebook[del_name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == 5:
        print("Exiting phonebook manager.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")







































    






   
















    





