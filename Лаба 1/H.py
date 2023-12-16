x = input("enter:")
list = x.split()#split-ділить речення на слова
answer = ""
for word in list:#Цикл, який бере по черзі слова і розвертає
    answer += word[: : -1] + " "#Беремо змінну word і все в змінній розвертаємо по слову і вписуємо в змінну answer
print(answer)