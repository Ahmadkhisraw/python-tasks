contacts = {}

def add_contact(name, number):
    contacts[name] = number

def search_contact(name):
    if name in contacts:
        return contacts[name]
    return "Not found"

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        return True
    return False

def edit_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return True
    return False

def display_contacts():
    for name, number in contacts.items():
        print(f"{name}: {number}")

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Edit contact")
    print("5. Display contacts")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == 2:
        name = input("Enter name: ")
        result = search_contact(name)
        print(result)
    elif choice == 3:
        name = input("Enter name: ")
        result = delete_contact(name)
        if result == True:
            print("contact found and deleted")
        else:
            print("contact not found")
    if choice == 4:
        name = input("Enter name: ")
        number = input("Enter number: ")
        result = edit_contact(name, number)
        if result == True:
            print("contact updated")
        else:
            print("contact not found")
    elif choice == 5:
        display_contacts()
    elif choice == 6:
        break
    