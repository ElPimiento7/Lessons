# Cписок, цикл for, цикл for с условиями, кортеж, множество, словарь, цикл for для словаря.

# Cписок. Содержит в себе элементы различного типа (Int, String, Float, Boolean...)
my_list = [1, 2, 5, "text", False, 123.3]  # Список пишется в квадратных скобках []
print(my_list[0])  # Выводит выбранный элемент из списка
my_list[1] = 42  # Заменяет и выводит выбранный элемент в списке
my_list.append("text")  # Добавляет элемент к списку
print(my_list)

# Цикл for
for element in my_list:  # Выводит каждый элемент по отдельности
    print(element)
# Цикл for с условиями
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in numbers:
    if x > 7:
        print(x * 2)
    elif x > 4:
        print(x * 3)
    else:
        print(x)

# Кортеж. В отличие от Списка, в кортеже нельзя изменять или добавлять элементы
my_tuple = (1, 2, 5, "text", False, 123.3)  # Кортеж пишется в круглых скобках ()
print(my_tuple[3])
for element in my_tuple:
    print(element)

# Множество. Нельзя получить элемент по индексу т.к, логика порядка другая, нельзя изменять элементы.
my_set = {1, 2, 5, "text", False, 123.3}  # Множество пишется в фигурных скобках {}
for element in my_set:
    print(element)
# Множество. Выводит уникальные значения
my_set2 = {1, 1, 1, 2, 5, 2, 6, False, False}
my_set2.add(345)  # Добавляет элемент
print(my_set2)

# Словарь. Передает элементы парами "Ключ": Значение
my_dict = {"name": "John", "age": 23, "nickname": "John007"}
print(my_dict["name"])  # Выводит значение элемента по ключу
my_dict["age"] = 30  # Меняет значение в выбранном ключе
my_dict["city"] = "New York"  # Добавляет новую пару "Ключ": Значение
print(my_dict)
# Цикл for для словаря
for element in my_dict:
    print(element)  # Выводятся только ключи

for key in my_dict:
    print(my_dict[key])  # Выводятся все значения из словаря

for key in my_dict:
    print(f"{key}: {my_dict[key]}")  # Выводит ключ и значение вместе

# ---------------------------------------------------------------------

e_colors = ["red", "green", "blue", "yellow", "purple", "brown"]
for element in e_colors:
    print(element)

e_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in e_numbers:
    if number < 6:
        print(number)

e_loop_with_conditions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in e_loop_with_conditions:
    if number % 2 == 0:
        print(number)

e_tuple = ("John", 23)
for element in e_tuple:
    print(element)

e_set = {"London", "Madrid", "Barcelona"}
for city in e_set:
    print(city)

e_dictionary = {"one": 1, "two": 2, "three": 3}
for key, value in e_dictionary.items():
    print(f"{key}: {value}")

# ---------------------------------------------------------------------

shop = {
    "products": [
        {
            "name": "Огурец средне плодный",
            "type": "Огурцы",
            "price": 10.0
        },
        {
            "name": "Красное яблоко",
            "type": "Яблоки",
            "price": 11.0
        },
        {
            "name": "Помидор",
            "type": "Томаты",
            "price": 12.0
        },
        {
            "name": "Болгарский перец",
            "type": "Перцы",
            "price": 15.0
        },
        {
            "name": "Огурец без пупырок",
            "type": "Огурцы",
            "price": 9.0
        }
    ]
}

for x in shop["products"]:  # Получаем словари на каждом цикле из элемента "Products"
    if (x["type"]) == "Огурцы":  # В каждом цикле достаем "Type" равный значению "Огурцы"
        x["price"] = x["price"] * 0.8  # Подменяем цену для "Price"

print(shop)
