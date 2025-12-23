contacts = {}

def add_contact():
    name = input("Enter Name: ")
    if name in contacts:
        print(f"Error: Contact '{name}' already exists.")
        return
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added successfully!")


def main_menu():
    """The main loop to interact with the contact book."""
    while True:
        print("\nWelcome to your Contact Book")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '5':
            print("Thank you for using the contact book!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
