from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
        pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() and len(value)!=10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                 self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.phones.append(Phone(new_phone))

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(name,num):
            pass


# Створення нової адресної книги
#book = AddressBook()

# Створення запису для John
john_record = Record("John")

john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
print(john_record)
john_record.edit_phone("5555555555","3332225556")

#john_record.remove_phone("5555555555")
print(john_record)
# Додавання запису John до адресної книги
##book.add_record(john_record)

# Створення та додавання нового запису для