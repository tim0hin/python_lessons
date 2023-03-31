# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Диапазон от 6 до 12

# Вывод: [1, 9, 13, 14, 19]
import random

def FindIndex(list):
    a, b = int(input("Диапазон от ")), int(input("Диапазон до "))
    listIdx = []

    for i in range(len(list)):
        if list[i] >= a and list[i] <= b:
            listIdx.append(i)

    return listIdx


list = [random.randint(-10, 10) for i in range(1, 20)]

print(list)
print(FindIndex(list))