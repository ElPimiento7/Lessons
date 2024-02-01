"""
 Инкапсуляция - Это механизм и способ организации классов когда мы данные и методы для работы с ними помещаем в одно
  место, но кроме того мы предоставляем пользователю публичное API для взаимодействия с нашим классом.

 Инкапсуляция подразумевает: 1. Все данные и методы для работы с ними находятся в одном месте. Т.е класс собирает данные
                                 и методы внутри себя. Это нужно для удобства, что бы пользователю не нужно было искать
                                 где находятся нужные методы, данные и т.д.
                             2. Предоставление пользователю публичного интерфейса (API). (Методы без подчеркиваний)
                             3. Не подразумевает сокрытие данных.
                             4. Публичный интерфейс (API) - Это контракт, все методы будут работать, внутренняя
                                 реализация не гарантируется (Для методов с любым подчеркиванием _, __).

    Совет! - Делать одно _ для внутренних атрибутов и реализаций, не перебарщивать с __ и сеттерами/геттерами.
"""

text = "1243124"
print(dir(text))
print([e for e in dir(text) if
       not e.startswith("_")])  # 2. В выводе получаю методы публичные, т.е те что без нижнего подчеркивания.
print("---------------------------------------------")


class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name  # 3. Одно нижнее подчеркивание _ (protected) подразумевает что атрибут не предназначен для прямого использования. Работа объекта не гарантируется, при использовании таких атрибутов.
        self._last_name = last_name
        self.__age = age  # Двойное нижнее подчеркивание __ (private) под капотом преобразуется в object. Class__attribute. (Только когда начинается с __). Name Mangling

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError("Age must be between 1 and 120")
        self.__age = age

    def describe(self):
        print(f"I am {self._first_name} {self._last_name}, I am {self.__age} years old!")


class First:
    def __init__(self):
        self._login = "sadfasf"
        self.__password = "password"


class Second(First):
    def __init__(self):
        super().__init__()
        self._login = "dfgdfgdfghjgjg"
        self.__password = "passsssss"


if __name__ == '__main__':
    ivan = Person("Ivan", "Pupkin", 23)
    # ivan._age = 1000
    ivan.set_age(110)
    ivan.describe()
    print(dir(ivan))
    print("---------------------------------------------")

    first = First()
    second = Second()
    print(first._login)
    print(second._login)
    print(second._First__password)
    print(second._Second__password)
