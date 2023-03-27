# Заменить максимальные оценки Василия на минимальные.
import random

def ChangeScores(array, n):
    array_new = [0]*n

    for i in range(n):
        if array[i] == max(array):
            array_new[i] == min(array)
        else:
            array_new[i] = array[i]
    
    return array_new


n = int(input("Введите количество оценок: "))

array = [random.randint(0, 10) for i in range(n)]

print(f"Начальный массив оценок: {array}")
print(f"Итоговые оценки: {ChangeScores(array, n)}")