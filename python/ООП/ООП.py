# #Класс - набор объектов, методов, атрибутов, выступающий  в роли контейнера (шаблона) для
# #будующего объекта, с которым работает уже пользователь
# #Объект - это воплощение требований, характеристик и качеств, которые приписываются конкретному классу
# class Car:
#     #Конструктор класса
#     def __init__(self, fuel, maxspeed):
#         self.fuel = fuel
#         self.maxspeed = maxspeed
#     #Функция для заправки топлива
#     def refuel(self, amount):
#         self.fuel += amount
#     #Функция для движения
#     def drive(self):
#         if self.fuel > 0:
#             print("Машина едет.")
#             self.fuel -=1
#         else:
#             print("Нет топлива.")
#
#
#
# polo = Car(50, 50)
# mini = Car(10,90)
# beetle = Car(0, 110)
# print("Сейчас будет двигаться polo")
# for i in range(10):
#     polo.drive()
# print("Сейчас будет двигаться mini")
# for i in range(10):
#     mini.drive()
# print("Сейчас будет двигаться beetle")
# for i in range(10):
#     beetle.drive()
#
# #Написать программу "Успеваемость студента". Пользователь вводит 10 оцекнок от 1 до 5. Реализовать меню для работы:
# #1) Вывод
# #2) Пересдача
# #3) Выходит ли стипендия?
# #4) Вывод отсортированных оценок по возврастанию и убыванию
# class Student:
#     def __init__(self, eval_list):
#         self.eval_list = eval_list
#     def menu(self):
#     while True
#         print("Меню: \n 1) Вывод \n"
#               "2) Пересдача \n"
#               "3) Стипендия \n"
#               "4) Вывод отсортированных оценок по возрастанию и убыванию"
#               "0) Выход")
#         print("*" *11)
#         value = int(input("Ваш выбор: "))
#         if value == 1:
#             self.Print() #Вывод функции вывода на экран
#     #Функция замены оценки
#     def reEval(self)
#         self.Print()
#         last_eval = int(input("ведите оценку на ЗАМЕНУ: "))
#         new_eval = int(input("Введите НОВУЮ оценку: "))
#         for i in range(len(self.eval_list)):
#             print()
#     #Функция вывода на экран
#     def Print(self):
#         print("Список оценок: "end=' ')
#         for i in self.eval_list:
#             print(i, end=' ')
#         print()
#     def ship(self):
#         if sum(self.eval_list)/len(self.eval_list) >=4:
#             print("Стипендия есть!")
#         else:
#             print("Низкий балл, не видать денежек :( ")
#     def sort_list(self):
#         if int(input("1 - Убывание, 2 - Возрастание \n Ваш выбор: "))
#             self.eval_list = sorted(self.eval_list, reverse=True)
#         else:
#             self.eval_list = sorted(self.eval_list)
#         print("Сортировка выполнена! Вот ваш список оценок: ")
#         self.Print()
#
# student = Student([1,5,3,4,2,3,5,5,5])
#
# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#     #При обращении методом-функцией, которая обрабатывает строки необходимо давать обращение встроенному методу
#     #__str__, который вернет строку для вывода/обработки
#     def __str__(self):

#Наследованиев ООП
# class Vehicle: #SUPER_CLASS, для нижестоящих классов
#     pass
# class LandVehicle(Vehicle): #Класс-наследник-подкласс
#     pass
# class TrackedVehicle(LandVehicle): #Класс-наследник-подкласс
#     pass
# # issubclass(OneClass, TwoClass) - функция для определения отношений между классами, проверка на наследование
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()
# # isinstance(objName, ClassName) = Проверка наличия у объекта определенных характеристик от класса наследника
# myVehicle = Vehicle()
# myLandVehicle = LandVehicle()
# myTrackVehicle = TrackedVehicle()
# for obj1 in [myVehicle, myLandVehicle, myTrackedVehicle]:
#     for cls2 in [myVehicle, myLandVehicle, myTrackedVehicle]:
#         print(isinstance(obj1, cls2), end='\t')
#     print()

#Пример2
# class SampleClass:
#     def __init__(self, value):
#         self.value = value
# obj1 = SampleClass(0)
# obj2 = SampleClass(10)
# obj3 = obj2
# obj3.value +=1
# print(obj1.value, obj2.value, obj3.value)
# #Оператор is позволяет определить, относятся ли две переменные, структуры или объекты к одному объекту класса
# print(obj1 is obj2)
# print(obj2 is obj3)
# print(obj3 is obj1)
#
# #Пример 3. Нахождение методов и атрибутов классов
# class Super:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f"Мое имя {self.name}, очень приятно"
# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
#
# #MAIN
# obj = sub("Михаил")
# print(obj)
#
# #Пример 4.
# slass Super:
#     supVar = 1
# class Sub(Super)
#     subVar = 2
#
# obj = sub()
# print(obj.supVar)
# print(obj.supVar)

#Пример 5.
# class Level1:
#     varial = 100
#     def __init__(self):
#         self.var1 = 101
#     def fun1(self):
#         return 102
# class Level2:
#     varial2 = 200
#     def __init__(self):
#         self.var2 = 201
#     def fun2(self):
#         return 202
# class Level3:
#     varial3 = 300
#     def __init__(self):
#         self.var3 = 301
#     def fun3(self):
#         return 302
# obj = Level3()
# print(obj.varial, obj.var1, obj.fun1())
# print(obj.varial2, obj.var2, obj.fun2())
# print(obj.varial3, obj.var3, obj.fun3())

#Пример 6. Множественное наследование
class SuperA:
    varA = 10
    def funA(self):
        return 11
class SuperB:
    varB = 20
    def funB(self):
        return 22
class SuperC:
    varC = 30
    def funC(self):
        return 33
class SuperD(SuperA,SuperB,SuperC):
    pass

#MAIN
obj = SuperD()
print(obj.varA, obj.varB, obj.varC)
print(obj.funA(), obj.funB, obj.funC)