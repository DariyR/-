text = input("Enter word:")
answer = ""

for word in text.split():
    answer += word * 2 + " "#додаємо перебране і помножене word + пробіл

print(answer.strip())#strip обрізає пробіли з початку і з кінця