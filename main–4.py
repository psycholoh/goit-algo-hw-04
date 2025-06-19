def parse_input(user_input):
    return user_input.strip().split()

def add_contact(command_parts, contacts):
    if len(command_parts) != 3:
        return "Invalid input. Use: add [name] [phone]"
    name, phone = command_parts[1], command_parts[2]
    contacts[name] = phone
    return "Contact added."

def change_contact(command_parts, contacts):
    if len(command_parts) != 3:
        return "Invalid input. Use: change [name] [phone]"
    name, phone = command_parts[1], command_parts[2]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(command_parts, contacts):
    if len(command_parts) != 2:
        return "Invalid input. Use: phone [name]"
    name = command_parts[1]
    if name in contacts:
        return f"{contacts[name]}"
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input(">>> ")
        command_parts = parse_input(user_input)

        if not command_parts:
            print("Invalid command.")
            continue

        command = command_parts[0].lower()
        result = ""

        if command == "add":
            result = add_contact(command_parts, contacts)
        elif command == "change":
            result = change_contact(command_parts, contacts)
        elif command == "phone":
            result = show_phone(command_parts, contacts)
        elif command == "all":
            result = show_all(contacts)
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            result = "Unknown command."

        if result:
            print(result)

if __name__ == "__main__":
    main()







