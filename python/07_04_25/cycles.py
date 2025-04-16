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
diametr = int(input("Введите диаметр окружности: "))
square = int(diametr/2 ** 2) * 3.14
perimetr = int(diametr/2 * 3.14)
print("Площадь окружности равна: ", square, "а периметр  равен: ", perimetr)

#Задание 3:
# price = int(input("Введите стоимость приставки: "))
# all = int(input("Введите количество приставок: "))
# discount = int(input("Введите процент скидки: "))