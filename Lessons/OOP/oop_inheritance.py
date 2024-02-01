"""
 Наследование - Это механизм получения доступа к данным и поведение своего предка. Он позволяет бороться с дублированием
                 кода, тем, что мы все общее выносим в класс предок Employee. А Python, позволяет обращаться к его
                 данным и к его методам.
                Позволяет, у наследовавшись от какого-то класса изменить или расширить его поведение не меняя код,
                 переопределив его методы.

 IS-A является (наследование)
 HAS-A содержит (композиция)
"""


class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 + self.bonus

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, salary: {self.salary}, bonus: {self.bonus}%, total bonus: {self.calculate_total_bonus()} rub"


class Cleaner(Employee):  # В скобках класс от которого наследуются данные и методы.
    def __init__(self, name):
        super().__init__(name, 15000, 1)  # super(). - Способ вызова у своего предка.


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)

    def calculate_total_bonus(
            self):  # Если в классе наследнике нужны дополнительные методы или переопределять методы от предка, они дописываются внутрь со своей логикой.
        return 200_000


def calc_bonuses(employees: list[Employee]):
    for employee in employees:
        print(f"Calc bonus for {employee.name}, it is {employee.calculate_total_bonus()}")


# --------------------------------------------------
class MyList(list):
    def __str__(self):
        return super().__str__().replace(",", ",\n")


if __name__ == '__main__':
    masha = Cleaner("Maria Ivanovna")
    print(masha)
    grisha = Manager("Grigoriy Petrovich")
    print(grisha)
    ivan = CEO("Ivan Pavlovich")
    print(ivan)
    a_list = [masha, grisha, ivan]
    calc_bonuses(a_list)
    print("----------------------------------------------")

    print([1, 2, 3])
    my_list = MyList([1, 2, 3])
    print(my_list)
    print(my_list[1])
    my_list.extend([4, 5])
    print(my_list)
    print(dir(my_list))
