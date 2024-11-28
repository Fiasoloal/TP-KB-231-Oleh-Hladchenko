class User:  
    def __init__(self, name, age, occupation, login, password):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.login = login
        self.password = password

    def __str__(self):  
        return f"Ім'я: {self.name}\nВік: {self.age}\nПрофесія: {self.occupation} \nЛогін: {self.login}\nПароль: {self.password}"

    def __repr__(self):  
        return f"User(name='{self.name}', age={self.age}, occupation='{self.occupation}', login='{self.login}', password='{self.password}')"


u = User("Vii", 19, "Student", "Vii$234", "12345")

print(u)
print(repr(u))
