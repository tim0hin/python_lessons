# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

def CloseToX(array, x):
    return min(array, key=lambda el: abs(el - x))


n = int(input("Укажите количество элементов в массиве: "))

array = [random.randint(0, 10) for i in range(n)]

print(*array)

x = int(input("Введите искомое число (x): "))

print(f"Близкое число из списка: {CloseToX(array, x)}")