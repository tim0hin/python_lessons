# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

def Answer(s, p):
    for i in range(s):
        for j in range(p):
            if i + j == s and i * j == p:
                print(f"x = {i}, y = {j}")
        

s, p = map(int, input("Введите сумму и произведение чисел через пробел: ").split())

Answer(s, p)