#for (УСЛОВИЕ):
    #ОПЕРАЦИЯ

# for i in range (10):
#     print("*" * i)

# for i in range (10, 100):
#     print("*" * i)

# sum = 0
# value = int(input("Введите число для ввода данных:"))
# for i in range(value):
#     sum = sum + int(input("Введите число: "))
#
# print(f'Сумма чисел пользователя: {sum}')
# print("Количество циклов получилось: ", i)

# for i in range(10):
#     print('%' * i)
#     for j in range(10):
#         print("*", end='')
#     print('\n')

# if strA == stringUser:
#     print("Строка палиндром!")
# else:
#     print("Строка - не палиндром!")
# strA = ''
# for i in stringUser:
#     strA = i + strA
# if strA == stringUser:
#     print()
# if stringUser == stringUser[::-1]:
#     print("Строка палиндром!")

#Метод среза строки
# stringA = "Hello world"
# a = stringA[6] # 'w'
# b = stringA[0:5] # 'Hello'
# c = stringA[0:5:2] # 'Hlo'
# d = stringA[0:5:-1] # 'olleH'
# stringB = "".json(reserved(stringA))
# stringC = ",".json(reserved(stringA)) #'H,e,l,l,o'
# stringB = "".split(reserved(stringA))

#Задание 1:
# time = int(input("Введите время, прошедшее с начала дня (с) от 0 до 86400: "))
# hour = (86400 - time) // 3600
# min = hour // 60
# sec = min // 60
# print("Оставшееся время ", hour, min, sec, sep=":")

#Задание 2:
# diametr = int(input("Введите диаметр окружности: "))
# square = int(diametr/2 ** 2) * 3.14
# perimetr = int(diametr/2 * 3.14)
# print("Площадь окружности равна: ", square, "а периметр  равен: ", perimetr)

#Задание 3:
# price = int(input("Введите стоимость приставки: "))
# all = int(input("Введите количество приставок: "))
# discount = int(input("Введите процент скидки: "))

#21/04/25
# num = int(input("Введите число от 1 до 9, которое я сейчас перемножу: "))
# for i in range(11):
#      print(num, "*", i, "=", num * i)

# val = input("укажите валюту (rub или tenge): ")
# sum = int(input("укажите сумму, которую необходимо конвертировать: "))
# if val == "rub":
#      print("Ваш номинал: РУБЛИ;", "сумма: ", sum, "сумма в тенге после конвертации: ", sum * 5)
# else:
#      print("Ваш номинал: ТЕНГЕ;", "сумма: ", sum, "сумма в рублях после конвертации: ", sum / 5)

diapazon1 = int(input("Введите первое число, определяющие начало границы диапазона: "))
diapazon2 = int(input("Введите второе число, определяющие конец границы диапазона: "))
number = int(input("Введите случайное число: "))
for i in range(diapazon1, diapazon2):
    if i == number:
        print(f"!{i}!", end=' ')
    else:
        print(i, end=' ')