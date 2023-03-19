# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random

def CountOfInverted(coins, n):
    eagles = 0
    tails = 0

    for i in range(n):
        if coins[i] == 0: tails += 1
        else: eagles +=1

    if eagles < tails: print(f"Минимальное количество монет, которые нужно перевернуть = {eagles}")
    else: print(f"Минимальное количество монет, которые нужно перевернуть = {tails}")


n = int(input("Укажите количество монеток: \n"))

coins = [random.randint(0, 1) for i in range(n)]    ## 1 - орёл, 0 - решка

print("Монетки: ")
print(*coins)

CountOfInverted(coins, n)