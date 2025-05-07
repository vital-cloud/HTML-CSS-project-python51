
#1)
# list = [-2,3,0,9,-7]
# sr_arifm = sum(list)/len(list)
# if sr_arifm > 0:
#     list1[-2,0,3]
#     list2[9,-7]
# elif sr_arifm < 0:
#     list1[-2,3]
#     list2[9,0,-7]

# #2)
# num = int(input())

import  random
def my_sort_one(mass):
    for j in range(len(mass)-1):
        for i in range(len(mass)-1):
            if mass[i] > mass[i+1]:
                mass[i],mass[i+1] = mass[i+1],mass[i]

def my_sort_two(mass):
    for j in range(len(mass)-1):
        for i in range(len(mass)-1):
            if mass[i] > mass[i+1]:
                mass[i],mass[i+1] = mass[i+1],mass[i]

mass = [random.randint(-10,10) for i in range(10)]
sr_z = sum(mass)/len(mass)
if sr_z < 0:
    my_sort_one(mass)
else:
    my_sort_two(mass)