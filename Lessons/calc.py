"""
# Перестановка цифр
a = int(input("Введи трехзначное число"))

d = a // 100
e = a % 100 // 10
f = a % 10

print(d, e, f, sep="")
print(d, f, e, sep="")
print(e, d, f, sep="")
print(e, f, d, sep="")
print(f, d, e, sep="")
print(f, e, d, sep="")


a = int(input())
print(f"Сумма цифр = {(a // 100) + (a % 100 // 10) + (a % 10)}")
print(f"Произведение цифр = {(a // 100) * (a % 100 // 10) * (a % 10)}")

print(a // 100)
print(a % 100 //10)
print(a % 10)


# Четырёхзначное число
a = int(input())
print(f"Цифра в позиции тысяч равна {a // 1000}")
print(f"Цифра в позиции сотен равна {a % 1000 // 100}")
print(f"Цифра в позиции десятков равна {a % 100 // 10}")
print(f"Цифра в позиции единиц равна {a % 10}")

a = int(input())
print(f"Цифра в позиции тысяч равна {a // 10000}")
print(f"Цифра в позиции единиц равна {a % 10000 // 1000}")
print(f"Цифра в позиции сотен равна {a % 1000 // 100}")
print(f"Цифра в позиции десятков равна {a % 100 // 10}")
print(f"Цифра в позиции единиц равна {a % 10}")


# Сумма квадратов VS квадрат суммы
a = int(input())
b = int(input())
print(f"Квадрат суммы {a} и {b} равен {(a + b) ** 2}")
print(f"Сумма квадратов {a} и {b} равна {a ** 2 + b ** 2}")

# Большое число
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a ** b + c ** d)


# Размножение n-ok
a = int(input())
print(a + a * 11 + a * 111)


# Пароль
password = input()
password_equal = input()

if password == password_equal:
    print("Пароль принят"),
else:
    print("Пароль не принят")


# Четное или нечетное?
number = int(input())

if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")


    # Соотношение
number = int(input())
if number // 1000 + number % 10 == number % 1000 // 100 - number % 100 // 10:
    print("ДА")
else:
    print("НЕТ")


# Роскомнадзор
age = int(input())
if age < 18:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")


# Арифметическая прогрессия
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
if num_2 - num_1 == num_3 - num_2:
    print("YES")
else:
    print("NO")


# Наименьшее из двух чисел
num_1 = int(input())
num_2 = int(input())
if num_1 < num_2:
    print(num_1)
else:
    print(num_2)


# Наименьшее из четырёх чисел
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

main_number = num1

if num2 < main_number:
    main_number = num2
if num3 < main_number:
    main_number = num3
if num4 < main_number:
    main_number = num4

print(main_number)


# Возрастная группа
age = int(input())
if age <= 13:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <= 59:
    print("зрелость")
if 60 <= age:
    print("старость")


# Только +
num1 = int(input())
num2 = int(input())
num3 = int(input())
zero = 0
if num1 > 0:
    zero = zero + num1
if num2 > 0:
    zero = zero + num2
if num3 > 0:
    zero = zero + num3
print(zero)

# Принадлежность
a = int(input())
if -1 < a < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")


# Принадлежность 2
num = int(input())
if num <= -3 or num >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")


# Принадлежность 3
num = int(input())
if -30 < num <= -2 or 7 < num <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")


# Красивое число
num = int(input())
if 1000 <= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
    print("YES")
else:
    print("NO")


# Неравенство треугольника
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
    print('YES')
else:
    print('NO')

    # Високосный год
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")

"""

# Ход ладьи
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if abs(num1 - num3) <= 1 and abs(num2 - num4) <= 1 and (num1 != num3 or num2 != num4):
    print("YES")
else:
    print("NO")





