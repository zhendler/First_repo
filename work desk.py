from collections import UserDict
import re
import datetime
import calendar

print("""
      'Hello! here is some command list:
      add contact - "add [name] [phone number]" 
      change contact - "change [name] [new phone number]"
      show contact - "show [name]"
      show all contacts - "all"
      add birth date - "add-birthday [name] [date of birth]" (DD.MM.YYYY)
      show date of birth - "show-birthday [name]"
      show all date of birth - "birthdays"
    	""")

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("Phone number must be 10 digits")

        valid_number = re.sub(r'[^\d+ ]', '', value)
        valid_number = valid_number.replace(' ', '') 
        while len(valid_number) > 10:
            valid_number = valid_number[1:]

        value = ('+38' + valid_number)
        super().__init__(value)

class Birthday(Field):
    def __init__(self, b_date):
        try:
            day, month, year = map(int, b_date.split('.'))
            self.value = datetime.date(year, month, day)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime('%d.%m.%Y')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, b_date):
        self.birthday = Birthday(b_date)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        old = Phone(old_phone)
        new = Phone(new_phone)

        for i, p in enumerate(self.phones):
            if p.value == old.value:
                self.phones[i] = new
                return
        raise ValueError("Phone number not found")

    def __str__(self):
        phones = ', '.join(phone.value for phone in self.phones)
        birthday = self.birthday.value.strftime('%d.%m.%Y') if self.birthday else "N/A"
        return f"Contact name: {self.name}, phones: {phones}, birthday: {birthday}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.date.today()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday.replace(year=today.year + 1)

                if today <= birthday_this_year <= today + datetime.timedelta(days=7):
                    weekday = calendar.weekday(birthday_this_year.year, birthday_this_year.month, birthday_this_year.day)
                    if weekday >= 5:
                        while calendar.weekday(birthday_this_year.year, birthday_this_year.month, birthday_this_year.day) >= 5:
                            birthday_this_year += datetime.timedelta(days=1)

                    upcoming_birthdays.append({"name": record.name.value, "birthday": birthday_this_year.strftime('%d.%m.%Y')})

        return upcoming_birthdays

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Invalid input.'
        except IndexError:
            return 'Invalid number of arguments.'
        except KeyError as e:
            return f"Contact '{e.args[0]}' not found."
    return inner

@input_error
def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        record.add_phone(phone)
        message = "Contact updated."
    return message

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return ', '.join(phone.value for phone in record.phones)
    return f"Contact '{name}' not found."

@input_error
def show_all_contacts(book):
    if not book:
        return "The phone book is empty."
    return str(book)

@input_error
def add_birthday(args, book):
    name, b_date = args
    record = book.find(name)
    if record:
        record.add_birthday(b_date)
        return "Birthday added."
    return f"Contact '{name}' not found."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return record.birthday.value.strftime('%d.%m.%Y')
    return f"Contact '{name}' not found or no birthday set."

@input_error
def birthdays(book):
    upcoming = book.get_upcoming_birthdays()
    return '\n'.join([f"{entry['name']}: {entry['birthday']}" for entry in upcoming])

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid number of arguments. Usage: add [name] [phone number]")
                continue
            print(add_contact(args, book))
        elif command == "change":
            if len(args) != 3:
                print("Invalid number of arguments. Usage: change [name] [old phone number] [new phone number]")
                continue
            name, old_phone, new_phone = args
            record = book.find(name)
            if record:
                try:
                    record.edit_phone(old_phone, new_phone)
                    print("Phone number updated.")
                except ValueError as e:
                    print(e)
            else:
                print(f"Contact '{name}' not found.")
        elif command == "show":
            if not args:
                print("Please specify a contact name.")
                continue
            print(show_phone(args, book))
        elif command == "all":
            print(show_all_contacts(book))
        elif command == "add-birthday":
            if len(args) != 2:
                print("Invalid number of arguments. Usage: add-birthday [name] [date of birth]")
                continue
            print(add_birthday(args, book))
        elif command == "show-birthday":
            if not args:
                print("Please specify a contact name.")
                continue
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        elif command in ("close", "exit"):
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
