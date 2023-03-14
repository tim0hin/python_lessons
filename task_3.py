# Программа находит простые делители числа

n = int(input('Введите число:\n'))

for num in range(2, n + 1):
    if n % num != 0:
        continue
    flag = True
    for spam in range(num - 1, 1, -1):
        if num % spam == 0:
            flag = False
            break
    if flag:
        print(num, end=' ')