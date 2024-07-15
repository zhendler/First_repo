print("""
      'Hello! here is some command list:
      add contact - "add [name] [phone number]" 
      change contact - "change [name] [new phone number]"
      show contact - "show [name]"
      show all contacts - "all"
        """)


def input_error(func):
    def inner(*arfg, **kwargs):
        try:
            return func(*arfg, **kwargs)
        except ValueError: #не дійсне значення
            return 'Give me name and phone pls.'
        except IndexError as e:  #не правильна кількість аргументів
            return f"Invalid number of arguments. Usage: {func.__name__} {e.args[0]}."
        except KeyError as e: #шья не знайдено
            return f"Contact '{e.args[0]}' not found."





@input_error
def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args

@input_error
def add_contact(contacts, name, phone):
        if name in contacts:
            return f"Contact '{name}' already exists."
        contacts[name] = phone
        return f"Contact '{name}' added."

@input_error
def change_contact(contacts, name, new_phone):
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = new_phone
    return f"Contact '{name}' phone number updated."

@input_error
def show_phone(contacts, name):
    if name not in contacts:
        return f"Contact '{name}' not found."
    return contacts[name]

@input_error
def show_all_contacts(contacts):
    if not contacts:
        print("The phone book is empty.")
        return
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():

    contacts = {} 

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid number of arguments. Usage: add [name] [phone number]")
                continue
            name, phone = args
            print(add_contact(contacts, name, phone))
        elif command == "change":
            if len(args) != 2:
                print("Invalid number of arguments. Usage: change [name] [new phone number]")
                continue
            name, new_phone = args
            print(change_contact(contacts, name, new_phone))
        elif command == "show":
            if not args:
                print("Please specify a contact name.")
                continue
            name = args[0]
            phone = show_phone(contacts, name)
            if phone:
                print(f"Phone number for '{name}': {phone}")
            else:
                print(f"Contact '{name}' not found.")
        elif command == "all":
            show_all_contacts(contacts)
        elif command in ("close", "exit"):
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

    