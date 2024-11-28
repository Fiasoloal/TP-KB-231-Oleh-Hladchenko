class Student:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Student name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"
