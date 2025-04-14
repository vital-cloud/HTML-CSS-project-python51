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

for i in range(10):
    print('%' * i)
    for j in range(10):
        print("*", end='')
    print('\n')