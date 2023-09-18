from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    # реалізація класу

class Phone(Field):
    def __init__(self, value):
        # Валідація номера телефону (10 цифр)
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Невірний формат номеру телефону")
        super().__init__(value)
    # реалізація класу

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Видалення телефону за значенням
        self.phones = [p for p in self.phones if str(p) != str(phone)]

    def edit_phone(self, old_phone, new_phone):
        # Редагування телефону
        for i, phone in enumerate(self.phones):
            if str(phone) == str(old_phone):
                self.phones[i] = Phone(new_phone)
                break
        else:
            raise ValueError("Номер телефону не знайдено у записі")
        
    def find_phone(self, phone):
        # Пошук першого телефону
        for p in self.phones:
            if str(p) == str(phone):
                return p
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"
    # реалізація класу


class AddressBook(UserDict):
    def add_record(self, record):
        # Додавання запису до адресної книги
        self.data[record.name.value] = record

    def find(self, name):
        # Пошук запису за іменем
        return self.data.get(name, None)

    def delete(self, name):
        # Видалення запису за іменем
        if name in self.data:
            del self.data[name]
    # реалізація класу