fibo = [0, 1]
i = 0
j = 1
index = 2

num = int(input("Введите число: ")) # ввод в консоли числа num и приведение его к типу int

while j < num:
    next_el = i + j
    fibo.append(next_el)    # метод append добавляет элемент в конец списка
    i = j
    j = next_el
    index += 1
print(fibo)

if j == num:
    print(index)
else:
    print(-1)   # когда число не является числом Фибоначчи, то выводим -1