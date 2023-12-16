import random

def is_palindrome(number):
    # Перевірка, чи є число поліндромом
    return str(number) == str(number)[::-1]

# Генеруємо 100 рандомних чисел в проміжку 1-1000
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Відбираємо поліндроми
palindromes = [num for num in random_numbers if is_palindrome(num)]

# Виводимо результати
print("Згенеровані числа:", random_numbers)
print("Поліндроми:", palindromes)