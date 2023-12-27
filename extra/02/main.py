contacts = {}

def add_contact(name, number):
    contacts[name] = number

def search_contact(name):
    if name in contacts:
        return contacts[name]
    return "Not found"

def display_contacts():
    for name, number in contacts.items():
        print(f"{name}: {number}")

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Display contacts")
    print("4. Exit")
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
        display_contacts()
    elif choice == 4:
        break
    