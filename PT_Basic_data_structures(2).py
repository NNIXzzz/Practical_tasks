#Дополнительное практическое задание по модулю
#Базовые структуры данных

grade = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # Оценки
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # Студенты

a1 = [sum(item) for item in grade] # Суммирование каждого элемента списка
b1 = [len(item) for item in grade] # Вычисление длины каждого элемента списка
result = [x / y for x, y in zip(a1, b1)] # Вычисление среднего балла студентов

sorted_students = sorted(students) # Сортировка студентов по алфавиту

student_average_score = dict(zip(sorted_students, result)) # Создание словаря из списков

print(student_average_score)

