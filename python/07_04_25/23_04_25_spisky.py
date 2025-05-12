#23/04/25
category = ['Drama', 'Comedy', 'Fantasy']
ls = []
var1, var2, var3 = 0, 0, 0
ls = list((var1, var2, var3))
#Вывод данных из списка
print(category)
for i in category:
    print(i)
for i in range(len(category)):
    print(category[i])
#Функции списка
ls3 = []
ls3.append(2) #Функция добавляет новый элемент в конец списка
print(ls3)
ls3.pop() #функция для удаления последнего элемента
#Если указать индекс в параметрах, будет удален элемент по индексу
#ls3.remove() #Удаление первого вхождения элемента
#ls3.clear() #Удаление всех элементов из списка
#category.index("Comedy") #Определение позиции элемента в списке
#category.count("Comedy") # 2 #Считает все вхождения элемента в список
#category.sort() #Выполняет сортировку элементов (по умолчанию по возрастанию)
#category.reverse() #Выполняет переворот списка
#Заполнение списков
import random
mylist = []
for i in range(10):
    mylist.append(random.randint(a:1, b:50))
print(mylist)
#Генератор списков
mylist2 = [i for i in range(10)]
#[значение + условие]
mylist3 = [i+"_" for i in "abcdefg"]
print(mylist3) #Выведет: a_b_c_d_e_f_g
mylist4 = [i*i for i in range(1,11) if i%2==0] #[4, 16, 36, 64,100]
customers = ['bob', 'anna', 'anton', 'max', 'nick', 'bob', 'joe']
customers2 = [i for i in customers if i!='bob' and i!='joe']
mylist5 = [x*y for x in range(10) for y in range(10)]
mylist5 = [[x * y for x in range(10)] for y in range(1,4)]
#Особенности списков, ссылки и клонирование
#Псевдонимы - это переменные, которые имеют  разные имена, но именют одинаковые адреса памяти
#Данная особенность важна, т.к. можно случайно, работая с одной переменной, испортить значения,
#хранящиеся в другой
list1 = [1,2,3,4,5]
print(list1)
#list2 = list1
list2 = list1.copy() #Копирование списка и присвоение ему нового контейнера
# list2 = list(list1)
print(list2)
list2[1] = 'Hello'
print(list2)
print(list1)
#Матрицы
#Нужны для хранения данных, представленных в виде пространств или таблиц
myTbl = [[111,112,113][221,222,223]]
print(myTbl[1][1])
for i in range(2):
    for j in range(2):
        print(myTbl[i][j])
#max(myTbl) #Находит максимальный элемент из списка
#sum(myTbl) #Получает сумму элементов списка
#min(myTbl) #Находит минимальный элемент списка
#print(mylist3[1:6])
#Пример:
#Пользователь вводит с клавиатуры элементы списка целых и некоторое число.
#Посчитать количество вхождений этого числа.
#Необходимо посчитать сумму всех четных элементов списка, среднее арнифметическое всех
#нечетных элементов списка.
#Результаты вывести на экран.
mylist = []
while true:
    value_user = int(input("Введите число для списка (0-выход):"))
    if value_user == 0:
        break
    else:
        mylist.append(value_user)
count_value_user = mylist.count(count_value)
for i in mylist:
    if i % 2 == 0:
        sum += i
nechet_list = [i for i in mylist if i % 2 != 0]
sred_arifm = sum(nechet_list) / len(nechet_list)
print(f"Кол-во элементов: {count_value user} \n"
      f"Сумма четных: {sum} \n"
      f"Средн. Арифм.: {sred_arifm}")
