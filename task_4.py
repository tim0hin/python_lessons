# Считает минимальный и максимальный вес арбузов

n = int(input("Введите количество арбузов в сетке: "))
watermellons = [0] * n
index = 0
while index < n:
    watermellons[index] = int(input("Введите массу арбуза в сетке: "))
    index +=1

print(f"Массы арбузов в сетке {watermellons}")

max = watermellons[0]
min = watermellons[0]
for i in watermellons:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"Масса самого тяжелого арбуза равна {max} кг")
print(f"Масса самого легкого арбуза равна {min} кг")