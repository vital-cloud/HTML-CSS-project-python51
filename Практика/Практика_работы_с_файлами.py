# Задание 1
# Дан тестовый файл. Необходимо создать новый файл, в который требуется переписать
# из исходного файла все слова, состоящие не менее чем из семи букв.
#1)
with open('text.txt', 'w') as f:
    f.write("banana mandarina mango me the lemonade math mango-banana guava-it-python")

buffer = ''
with open('text.txt', 'r') as f:
    buffer = f.readline()

buffer_list = buffer.split(" ")
with open("text_result.txt", 'w') as f:
    for i in range(len(buffer_list)-1):
        if len(buffer_list[i]) >=7:
            f.writelines(buffer_list[i]+"\n")

# Задание 2
# Дан текстовый файл. Необходимо переписать его строки в другой файл.
# Порядок строк во втором файле должен совпадать с порядком строк в заданном файле.
#2)
with open('text_result.txt',"r") as f:
    with open('new_text_result.txt',"w") as fi:
        fi.writelines(f.readlines())

# Задание 3
# Дан текстовый файл. Необходимо переписать его строки в другой файл. Порядок строк
# во втором файле должен быть обратным по отношению к порядку строк в заданном файле.
#3) Переделать!
with open('text_result.txt',"r") as f:
    with open('new_text_result.txt',"w") as fi:

        one_text = reversed(fi.writelines(f.readlines()))


# Задание 4
# Дан текстовый файл. Добавить в него строку из двенадцати звездочек (************),
# поместив ее последней из строк, в которой нет запятой. Если таких строк нет,
# то новая строка должна быть добавлена после всех строк имеющегося файла.
# Результат записать в другой файл.
#4)

