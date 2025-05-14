#Кортеж - неизменяемая структура данных, которая по своему подобию похожа на список.
#Список - изменяемый тип данных [1,2,3]
#a = [1,2,3]
#a[1] = 5
#print(a)
#b = (1,2,3)
#b[1] = 15 #Ошибка TypeError
#print(b)
#Плюсы:
#1) Экономия места (в 32 раза меньше по весу чем список)
#2) В процессе работы, данные в безопасности
#3) Выше производительность системы

a = (1,2,3)
print(type(a)) #class typle
print(a[1]) #2
del a #Отдельно элемент не удалить, только сам объект
lst = [1,2,3,4,5]
print(type(lst))
tpl = tuple(lst)
print(type(tpl))
print(tpl)
#Обратно:
lst2 = list(tpl)
print(type(lst2))
print(lst2)

#Словари (dict)
#Словарь - это неупорядоченная структура данных, которая позволяет хранить в себе
#данные в формате пар:
# "Ключ": "Значение"
dictionary = {"Персона":"Человек",
              "Марафон":"Гонка бегунов длиной около 26 миль",
              "Айфон":15}
dictionary2 = {(1,1.2,0.2):"ортежи могут быть ключами",
               1:"Целые числа тоже могут быть ключами",
               "БЕЖАТЬ":"Строки тоже",
               #['носок',1,5]:"а списки не могут"
               }
#Не работают нехэшируемые типы данных
dictionary3 = {True:'yes',1:'no',1.0:'maybe'}

#Работа со словарями:
d = {}
d = {'dict_key':'dict_value'}
d = dict(short='dict', long='dictyonary')
d['index'] = 20 #Самая короткая запись объявления словаря
d = dict.fromkeys(['a','b'],100)
key_list = ['marvel','dc']
value_list = ['Spiderman','Flash']
superhero_list = dict(zip(key_list, value_list))
d = {i : i*2 for i in range(10)} #Генератор словарей
print(d)

#Получение данных из словаря:
dictionary4 = {"Марафон":26}
print(dictionary4['Марафон']) #Получение значений
# Будет ошибка, если ключей не существует
# Для лучшего исхода лучше использовать метод *.get()
# Для удаления данных используется метод del dictionary4['Марафон']
# d.clear() #Очищает словарь от всех пар, но не удаляет переменную
# d.copy()
## d = distionary
## id(d) #12345678
## id(dictionary) #12345678
#dictionary4.get('Марафон') #26
#d.update()
dictionary = {"Персона":"Человек",
              "Марафон":"Гонка бегунов длиной около 26 миль",
              "Айфон":15}
dictionary.update({"Марафон":"33km","Айфон":11})
#d.pop(key) #Удаляет ключ и возвращает его значение
#d.setdefault("name") #Ищет ключ и возвращает его значение,
# если он не найдет - создает этот ключ со значением None
#d.keys() #Возвращает список ключей в словаре
#d.values() #Возвращает список значений словаря
#d.items() #Возвращает пары ключ:значение

#Примеры:
#1. Итерация через консоль
story_dict = {"Сто":100, "Двести":200, "Триста":300}
for key in story_dict:
    print(key)
for key, value in story_dict.items():
    print(key, value)

#Сортировка словаря:
people = {3:'jim',
          4:'olga',
          1:'max',
          5:'ivan',
          6:'kirill'}
print(sorted(people))
import itertools

#Если задача состоит в том, что словарь слишком большой, а вам нужнга лишь его часть,
#вам поможет метод islice()
nd = dict(itertools.islice(people.items(), 0, 3))
print(nd)

#dict to list (Преобразование)
people_list = []
for key, value in people.items():
    temp = [key, value]
    people_list.append(temp)
#p_l = [[key,value] for key, value in people.items()]

#Множества(set) - контейнер, содержащий не повторяющиеся элементы в случайном порядке
#Создание множества
s = set()
print(type(s)) #class set
s = set('hello')
print(s)
# {'h','e','l','l','o'}
s = {i **2 for i in range(10)}
print(s)

#Методы set
# len()
# x in s #Проверка принадлежности
#s.isdisjoint(other) - истина, если set и other не имеют общих элементов
# set == other -проверка всех элементов множества не пересечение с другим множеством
# s.issubset(other) -проверка принадлежности множества
# s.issuperset(other) -проверка второго множества на вхождение в первое
# s.union(other, ...) #объединение нескольких множеств
# s.intersection(other) -пересечение множеств
# s.difference() -Множество элементов, уникальных в двух множествах (не пересекаются)
# s.symmetric_difference() -уникальные встречающиеся элементов
# s.copy()
# s.update(other)
# s.intersection_update(other)
# s.difference_update(other)
# s.simmetric_difference_update(other)
# s.add(item) -Добавление элемента
# s.remove(item) -Удаление элемента
# s.discard(item) -Удаление элемента, если он есть в множестве
# s.pop() -Удаляет случайный элемент
# s.clear() -Очистка множества

# Пример "Задача инвестора"
our_products = {"Apple","Tesla","DNS"}
range_of_company_1 = {"Samsung","Sony"}
range_of_company_2 = {"Apple","BMW","IBM"}
range_of_company_3 = {"BMW","Tesla","DNS","Ferrary"}
#Акции, которые уже есть у нас в 3х списках:
print("Акции, которые уже есть у нас в 3х списках")
print(our_products.intersection(range_of_company_1))
print(our_products.intersection(range_of_company_2))
print(our_products.intersection(range_of_company_3))
#Противоположная задача:
print("Акции, которых у нас нет в 3х списках")
print(our_products.difference(range_of_company_1))
print(our_products.difference(range_of_company_2))
print(our_products.difference(range_of_company_3))
#Разница в товарах:
print("Разница в 3х списках")
print(our_products.symmetric_difference(range_of_company_1))
print(our_products.symmetric_difference(range_of_company_2))
print(our_products.symmetric_difference(range_of_company_3))

frozenset_product = frozenset(our_products) #Замороженный портфель, неизменяемый контейнер

#Пример 2 "Журнал Юзера"
my_dict = {"Nikita":{
                "tel":"12345678910",
                "OK":"ok.ru/nikita41",
                "vk":"vk.com/nikitaaa",
                "nick":"Друг детства"
                    },
            "Marina":{
                "tel":"22345678910",
                "OK":"ok.ru/marina41",
                "vk":"vk.com/marinaaa",
                "nick":"Подруга детства"
                    },
            "Max":{
                "tel":"32345678910",
                "OK":"ok.ru/max41",
                "vk":"vk.com/maxxx",
                "nick":"Товарищ"
                }
            }
user = my_dict[input("Введите имя пользователя: ")][input("Что конкретно? -->")]
print(user)