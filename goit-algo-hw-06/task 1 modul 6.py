from collections import UserDict
import re
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
        if not value.isdigit():
            raise ValueError("Phone number must be 10 digits")

        valid_number=re.sub(r'[^\d+ ]','',value)
        valid_number=valid_number.replace(' ','') 
        while len(valid_number)>10:
            valid_number=valid_number[1:]

        value = ('+38' + valid_number )
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, b_date):
        pass

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                 self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        old = Phone(old_phone)
        new = Phone(new_phone)

        for p in self.phones:
            if p.value== old.value:
                self.phones.remove(p)
                self.phones.append(new)
            else:
                raise ValueError("Phone number not found")

    def find_phone(self,phone):
        f_phone=Phone(phone)
        for p in self.phones:
            if p == f_phone:
                print (f"{self.name}: {f_phone.value}")
        return None


    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):

        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    @input_error
    def add_birthday(args, book):
        # реалізація
        pass

    @input_error
    def show_birthday(args, book):
        # реалізація
        pass
    @input_error
    def birthdays(args, book):
        # реалізація
        pass

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())



book = AddressBook()


john_record = Record("John")
jane_record = Record("Jane")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
jane_record.add_phone("6666666666")
#print(john_record)
#john_record.edit_phone("1234567890","0987654321")
#john_record.find_phone("1234587890")
#john_record.remove_phone("5555555555")
#print(john_record)

book.add_record(john_record)

book.add_record(jane_record)


#print(book)

# Find and edit John's phone
john = book.find("John")

#print(john)  



book.delete("Jane")


#print(book)