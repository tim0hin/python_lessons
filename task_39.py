# Вывести элементы списка А, которых нет в списке B

n = int(input())  # количество элементов в первом массиве
a = list(map(int, input().split()))  # первый массив
if len(a) != n:
    print("Некорректный ввод первого массива")
    exit()
m = int(input())  # количество элементов во втором массиве
b = set(map(int, input().split()))  # второй массив
if len(b) != m:
    print("Некорректный ввод второго массива")
    exit()

for x in a:
    if x not in b:
        print(x, end=' ')