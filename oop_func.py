class Person:

    def __init__(self, name, age, gender):

        self.name = name

        self.age = age

        self.gender = gender

    def introduce(self):

        print(f'I am {self.name} by name,{self.age} years old and a {self.gender}.')


persons = Person('Max', 65, 'male')
persons.introduce()

