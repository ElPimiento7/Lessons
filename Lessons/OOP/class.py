# Классы - это группа объектов имеющая общие характеристики и возможности
import math


class Birds:  # Задаются характеристики для класса. Названия классов пишутся с большой буквы
    wings = True
    beak = True
    plumage = True

    def fly(self):  # Метод
        print("I am flying")

    def walk(self):  # Метод walk существует у любой птицы, а, в подклассе этот метод нужно реализовать правильно т.к
        pass  # каждый метод у разных птиц разный


# В методах указываются общие характеристики

class Sparrow(Birds):  # Подкласс родительского класса Birds
    size = "small"

    def walk(self):
        print("I am jumping")


class Duck(Birds):

    def walk(self):
        print("I am walking")


# В методах подкласса указываются характеристики принадлежащие только подклассу


chizik = Sparrow()
pyzhik = Sparrow()
utka = Duck()
pyzhik.size = "medium"

print(chizik.size)
print(pyzhik.size)
pyzhik.walk()
chizik.fly()
utka.walk()


# ---------------------------------------------------------------------------------------------------------------------


class Person:
    name = "Ivan"
    age = 23

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years")


person = Person()
person.introduce()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_radius(self):
        print(f"The radius is {self.radius}")

    def area(self):
        return math.pi * self.radius ** 2


circle = Circle(100)
circle.display_radius()
print(f"The area is {circle.area()}")


class Rectangle:
    width = 23
    height = 40

    def area(self):
        print(f"The area is {self.width * self.height}cm")


rect = Rectangle()
rect.area()


class Cat:
    name = "Shaggy"
    color = "grey"

    def meow(self):
        print("МЯЯЯУ!")


cat = Cat()
print(cat.name)
print(cat.color)
cat.meow()


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def summ(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


calc = Calculator(10, 5)
print(f"Sum: {calc.summ()}")
print(f"Subtract: {calc.subtract()}")
print(f"Multiply: {calc.multiply()}")
print(f"Divide: {calc.divide()}")
