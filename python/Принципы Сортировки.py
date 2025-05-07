import random
#Пузырьковая сортировка
def bubble_sort(mass):
    #Для выполнения алгоритма, необходимо сравнить 2 элемента
    #массива друг с другом, если первый элемент больше второго, то
    #мы их меняем местами. Процесс продолжается до последней пары элементов
    #сравнения. Алгоритм провторяется n^2 раз, даже, если массив уже отсортирован.
    swapped = True #ужна для запуска сортировки 1 раз.
    while swapped:
        swapped = False
        for i in range(len(mass) - 1):
            if mass[i] > mass[i+1]: #Проверка элементов
                mass[i],mass[i+1] = mass[i+1],mass[i] #Свап
                swapped = True #Возвращаем значение для дальнейших итераций
#Сортировка выборкой - делит список на две части: отсортированную
#и неотсортированную. В качестве него используется крайняя левая часть списка.
#Находится наименьший элемент и меняется с первым элементом местами.
def selection_sort(mass):
    for i in range(len(mass)):
        # i - значение соответствует кол-во отсортированных

def heapify(mass, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    #Если левый потом корня - допустимый индекс, а элемент больше, чем текущий наибольший,
    #обновляем элемент
    if left_child < heap_size and mass[left_child] > mass[largest]:
        largest = left_child
    #Точно также проверяем правый корень
    if right_child < heap_size and mass[right_child] > mass[largest]:
        largest = right_child
    #Если наибольший элемент больше не является\ корнем дерева, то они меняются местами
    if largest != root_index:
        mass[root_index], mass[largest] = mass[largest], mass[root_index]
        heapify(mass, heap_size, largest)
def heap_sort(mass):
    n = len(mass)
    for i in range(n, -1, 1):
        heapify(mass, n, i)
    #Перемещаем корень Max Heap в конец списка
    for i in range(n-1, 0, -1):
        mass[0], mass[i] = mass[i], mass[0]
        heapify(mass, i, 0)