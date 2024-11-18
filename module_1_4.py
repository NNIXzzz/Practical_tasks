#Практическая работа по уроку "Организация программ и методы строк"

my_string = input('Кличка Вашего домашнего питомца: ')
count = my_string.count('', 1)
print(count)

# В верхнем регистре

print(my_string.upper())

# В нижнем регистре

print(my_string.lower())

# Удалив все пробелы

print(my_string.replace(' ', ''))

# Первый символ строки

print(my_string[0])

# Последний символ строки

print(my_string[-1])