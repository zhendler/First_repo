def parse_input(user_input):
    """
    Розбиває введений користувачем рядок на команду та аргументи.

    Args:
        user_input (str): Рядок введений користувачем.

    Returns:
        tuple: Кортеж, що містить команду та список аргументів.
    """
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args


def add_contact(contacts, name, phone):
    """
    Додає новий контакт до телефонної книги.

    Args:
        contacts (dict): Словник, що містить контакти.
        name (str): Ім'я нового контакту.
        phone (str): Номер телефону нового контакту.

    Returns:
        str: Повідомлення про результат додавання контакту.
    """
    if name in contacts:
        return f"Contact '{name}' already exists."
    contacts[name] = phone
    return f"Contact '{name}' added."


def change_contact(contacts, name, new_phone):
    """
    Змінює номер телефону існуючого контакту.

    Args:
        contacts (dict): Словник, що містить контакти.
        name (str): Ім'я контакту, номер якого потрібно змінити.
        new_phone (str): Новий номер телефону.

    Returns:
        str: Повідомлення про результат зміни номера телефону.
    """
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = new_phone
    return f"Contact '{name}' phone number updated."


def show_phone(contacts, name):
    """
    Виводить номер телефону вказаного контакту.

    Args:
        contacts (dict): Словник, що містить контакти.
        name (str): Ім'я контакту.

    Returns:
        str: Номер телефону контакту або повідомлення про помилку.
    """
    if name not in contacts:
        return f"Contact '{name}' not found."
    return contacts[name]


def show_all_contacts(contacts):
    """
    Виводить список усіх контактів та їх номерів телефонів.

    Args:
        contacts (dict): Словник, що містить контакти.
    """
    if not contacts:
        print("The phone book is empty.")
        return
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    """
    Основна функція чат-бота.
    """
    contacts = {}  # Словник для зберігання контактів

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
        elif command == "phone":
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