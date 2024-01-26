def hello(name):
    if name == "":
        print("Hello World!")
    else:
        print(f"Hello {name}")


def hello2(name):
    if name:
        print(f"Hello {name}")
    else:
        print("Hello World!")

# -------------------------------------------------------------------------

# print("Введите 2 числа, каждое из которых не больше 10")
# x = int(input("Первое число: "))
# y = int(input("Первое второе: "))

def divide(x, y):
    if x > 10 or y > 10:
        result = "Число не соответствует требованиям"
    elif y == 0:
        result = "Не дели на ноль"
    else:
        result = x / y
    return result

def divide2(x, y):
    if x > 10 or y > 10:
        return "Число не соответствует требованиям"
    if y == 0:
        return "Не дели на ноль"
    return x / y


print(divide2(6, 0))


lst = [1, 2, 3, 4, 5, 6, 7]

new_lst = []
for i in lst:
    new_lst.append(i * 2)

new_lst = [i * 2 for i in lst]

new_lst2 = []
for i in lst:
    if i % 2 == 0:
        new_lst2.append(i)

new_lst2 = [i for i in lst if i % 2 == 0]

print(new_lst2)

i = 0
while i < 20:
    print("Hello")
    i += 1

for _ in range(20):
    print("World")


tpl = ("ONE", "TWO", "THREE")
var1, var2, var3 = tpl
print(var1, var2, var3)
