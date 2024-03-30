def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(contacts, name, phone_number):
    contacts[name] = phone_number
    return "Contact added."

def change_contact(contacts, name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(contacts, args[0], args[1]))
            else:
                print("Invalid command. Usage: add [name] [phone_number]")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(contacts, args[0], args[1]))
            else:
                print("Invalid command. Usage: change [name] [new_phone_number]")
        elif command == "phone":
            if len(args) == 1:
                print(show_phone(contacts, args[0]))
            else:
                print("Invalid command. Usage: phone [name]")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
