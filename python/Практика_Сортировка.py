#Есть стопка оладий различного радиуса. Единственная операция, проводимая с ними -
#между двумя любыми оладьями просовываем лопатку и меняем порядок оладий на обратный.
#Необходимо за минимальное количество таких операций отсортировать снизу вверх
#по убыванию радиуса оладья:

# def pancakes_sort(mass):
#     #Поиск индекса максимального элемента
#     def find_largest_index(mass, n):
#         i = 0
#         for j in range(n):
#             if mass[j] > mass[i]:
#                 i = j
#         return i
#     #Функция переворачивания блинчика
#     def flip(mass, k):
#         return mass[:k][::-1] + mass[k:]
#     result = []
#     n = len(mass)
#     while n > 1:
#         i = find_largest_index(mass, n)
#         if i < n-1:
#             mass = flip(mass, i+1)
#             result.append(i+1)
#             mass = flip(mass, n)
#             result.append(n)
#         n -= 1
#     return result
# pancakes = [3,1,4,5,9,6,4,3,6,2,4,7]
# oper = pancakes_sort(pancakes)
# print("Блины:",pancakes)
# print("операции:",oper)

#1)
# import  random
#
# my_sort_1 = [random.randint(0,10)]
# print(my_sort_1)
# my_sort_2 = random[0, 10]
# print(my_sort_2)


import random
mylist1 = []
for i in range(10):
    mylist1.append(random.randint(1, 10))
print(mylist1)
mylist2 = []
for i in range(10):
    mylist2.append(random.randint(11, 20))
print(mylist2)
mylist3 = []
for i in range(10):
    mylist3.append(random.randint(21, 30))
print(mylist3)
mylist4 = []
for i in range(10):
    mylist4.append(random.randint(31, 40))
print(mylist4)
mylist5 = mylist1 + mylist2 + mylist3 + mylist4
print(mylist5)
press = input("Отсортировать по возрастанию (+), или по убыванию (-) ??? ")
if press == "+":
    print("+")
elif press == "-":
    print("-")
else:
    print("Только + или - !!!")