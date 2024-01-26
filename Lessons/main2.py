print("Hello World!")

name = input("Как тебя зовут? ")
print(f"Hello {name}")

print("Сумма двух чисел")
a = int(input("Введи первое число"))
b = int(input("Введи второе число"))
result = a + b
print(f"{a} + {b} = {result}")

print("Умножение двух чисел")
a = int(input("Введи первое число"))
b = int(input("Введи второе число"))
result = a * b
print(f"{a} x {b} = {result}")

print("Возведение в степень")
a = int(input("Введи число"))
result = a ** 2
print(f"{a} возведенное в степень = {result}")

text = input("Введи любой текст ")
print(text)

print("Арифметические операции +-*/")
a = int(input("Введи первое число"))
b = int(input("Введи второе число"))
sum_result = a + b
difference_result = a - b
multiplication_result = a * b
division_result = a / b
if b != 0:
    print(f"{a} + {b} = {sum_result}")
    print(f"{a} - {b} = {difference_result}")
    print(f"{a} * {b} = {multiplication_result}")
    print(f"{a} / {b} = {division_result}")
else:
    print("Деление на 0 не возможно.")
