# #Калькулятор
# value1 = int(input("Введите первую переменную:"))
# value2 = int(input("Введите вторую переменную:"))
# print(f"{value1} + {value2}={value1 + value2}")#Сумма элементов
# print(value1 + value2)#Сумма элементов
# #string - тип данных для текста
# #int -тип данных для целочисленных чисел
# #float- тип данных с плавающей точкой
# #boot -  тип данных логический, True, False
# print(f"{value1} - {value2} = {value1 - value2}")
# print(f"{value1} * {value2} = {value1 * value2}")
# print(f"{value1} / {value2} = {value1 / value2}")
# print(f"{value1} // {value2} = {value1 // value2}")
# print(f"{value1} % {value2} = {value1 % value2}")
# print(f"{value1} ** {value2} = {value1 ** value2}")
# print("*" * 11)
# #Проверка и сравнение данных
# print(value1 > value2)
# print(value1 < value2)
# print(value1 == value2)
# print(value1 == 'Hello World!!!')#Проверка на равенство
# print(value1 != 'Hello World!!!')#Проверка на неравенство
# print("hello" > "hello world!!!")

#Пользователь вводит с клавиатуры три числа.
#Необходимо найти сумму чисел, произведение чисел.
#Результат вычислений вывести на экран.
# value_number = int(input("Введите число 1:"))
# value_number2 = int(input("Введите число 2:"))
# value_number3 = int(input("Введите число 3:"))
# sum = value_number + value_number2 + value_number3
# proz = value_number * value_number2 * value_number3
# print(f"Сумма: {sum}")
# print(f"Произведение: {proz}")

#Пользователь вводит с клавиатуры три числа.
#Первое число - зарплата за месяц.
#Второе число - сумма ежемесячного платежа по кредиту в банке.
#Третье число - задолженность за коммунальные услуги.
#Необходимо найти сумму, которая останется у пользователя после всех выплат.
# value_number = int(input("Введите зарплату: "))
# value_number2 = int(input("Введите платеж по кредиту: "))
# value_number3 = int(input("Введите коммуналку:"))
# result = value_number - value_number2 - value_number3
# print(f" ЗП: {value_number}, \n"
#       f" Платеж: {value_number2}, \n"
#       f" Коммуналка: {value_number3}"
#       f" Остаток: {result}")
#
# #Экранирование символов
# #Вызов спец символа \ для создания комманды вставки символов
# # \\ - Добавляет обратный слеш
# # \" - Добавляет двойные кавычки
# # \' - Добавляет одинарные кавычки
# # \n - Переносит на новую строку
# # \t - Вставка 3х пробелов
# # \b - Удаляет предыдущий символ
# string = "Фраза для работы со строкой"
# print(value_number, string, value_number2, value_number3, sep="*\n")
# #sep - это строка для вставки между значениями элементов вывода для print
# #end - это вставка символа в конце строки, вместо \n
# print(value_number, string, value_number2, value_number3, end="***")

# value1 = ("To be")
# value2 = ("or not")
# value3 = ("to be")
# print(value1, "\n", "\t", "\t", value2, "\n", "\t", "\t", "\t", "\t",value3)
# print("To be", "\n", "or not", "\n", "\t", "to be")

#Пользователь вводит с клавиатуры три цифры
# Необходимо создать число, содержащее эти цифры
# Например, если с клавиатуры введено 1, 5, 7
# Тогда нужно сформировать число 157
# value_number1 = int(input("Введите число 1:"))
# value_number2 = int(input("Введите число 2:"))
# value_number3 = int(input("Введите число 3:"))
# print(value_number1,value_number2,value_number3)

# a = int(input())
# b = int(input())
# c = int(input())
# print(a*100+b*10+c)
# print(str(a)+str(b)+str(c))
# print(str(a)+str(b)+str(c), sep='')

# Позьзователь вводит с клавиатуры число, состоящее из четырех цифр
# требуется найти произведение цифр
# Например если с клавиатуры введено 1234
# тогда результат произведения 1*2*3*4
# a = int(input())
# print( (a//1000)*((a//100)%10)*((a//10)%10)*(a % 10))
#
# a = input()
# print(int(a[0])*int(a[1])*int(a[2])*int(a[3]))
#
# Строки и их свойства
string = "my Name is AaA"
print(type(strong)) #Проверка типа данных
print(string + srting) #Сложение строк
print(string * 4) #Умножение строк
print(srting.capitalize()) #Приводит первую букву в верхний регистр (только первую!)
print(srting.lower()) #Приводит все символы в нижний регистр
print(srting.swapcase()) #Меняет текущий регистр буквы на противоположный
print(srting.title()) #Преобразует первые буквы всех слов в верхний регистр
print(srting.upper()) #преобразует все буквы в верхний регистр
print(srting.count("my", start=0, end=5)) #Подсчитывает количество элементов в строке (start, end можно не писать)
print(srting.endswith("!")) #Проверяет, заканчивается ли строка подстрокой
print(srting.startswith("!")) #Проверяет, начинается ли строка подстрокой
print(srting.find("is")) #Ищет подстроку в строке, слева направо
print(srting.rfind("AaA")) #Ищет подстроку в строке, справо налево
#Возвращает первое вхождение (индекс) подстроки
print(srting.index()) #Ищет подстроку в строке, слева направо
print(srting.rindex()) #Ищет подстроку в строке, справо налево
#Возвращает первое вхождение (индекс) подстроки. Если элемента нет, выдаст ошибку

#Классификация (определение) строк
print(string.isalnum()) #Определяет, состоит ли строка из букв и чисел
print(string.isalpha()) #Определяет, состоит ли строка из букв
print(string.isdigit()) #Определяет, состоит ли строка из чисел
print(srting.slower()) #
print(srting.isupper()) #
print(srting.istitle()) #
print(srting.isspace()) #Проверяет наличие в строке пробельных символов

#Форматирование и выравнивание строк
print("main".center(10, "*")) #Выравнивание строки по центру
print("main\t\t\t main".expandtabs(tabsize=8)) #Заменяет табуляцию на пробелы
print("main maim".ljust(10, "@")) #Выравнивание по левому краю
print("main maim".ljust(10, "?")) #Выравнивание по правому краю
print("main main".lstrip()) #Все пробельные символы с левого края будут удалены
print("main main".rstrip()) #Все пробельные символы с правого края будут удалены
print("main main".replace("main", "own")) #Заменяет подстроку