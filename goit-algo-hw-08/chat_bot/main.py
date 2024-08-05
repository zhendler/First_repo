from addressbook import AddressBook
from commands import add_contact, show_phone, show_all_contacts, add_birthday, show_birthday, birthdays
from input_error import parse_input
from load_saver import save_data , load_data

def main():
    book = load_data()

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
            save_data(book)
        elif command == "show":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
            save_data(book)
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        elif command in ("close", "exit"):
            print("Good bye!")
            save_data(book)
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
