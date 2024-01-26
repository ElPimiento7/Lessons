class Person:
    def __init__(self, name, age, weigh, country, gender=None):
        self.name = name
        self.age = age
        self.weigh = weigh
        self.country = country
        self.gender = gender

    def say_name(self):
        print(f"My name is {self.name}. I am {self.age} years and I am from {self.country}")


person_one = Person("Antonio", 35, 79, "Span", "Male")
person_two = Person("Gustavo", 43, 85, "Italia")

print(person_one)
print(person_one.name, person_one.age, person_one.weigh, person_one.country, person_one.gender)
person_one.say_name()
print(person_two)
print(person_two.name, person_two.age, person_two.weigh, person_two.country, person_two.gender)
person_two.say_name()