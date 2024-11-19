#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

#Кортеж

immutable_var = 12, 34,'home', 'work'
print(immutable_var)

immutable_var = (12, 34, 'home', 'work')
#immutable_var[0] = 1234
#print(immutable_var) Изменение кортежа невозможно, по причине его постоянства.

immutable_var = (12, [34, 'home'], 'work')
immutable_var[1][0] = 1234
immutable_var[1][1] = 'house'
print(immutable_var) # Изменение кортежа возможно лишь с наличием в нём списка. Причём изменить можно лишь сам список.

#Список

mutable_list = [12, 34, 'home', 'work']
print(mutable_list)

mutable_list[0] = 1234
mutable_list[2] = 'house'
print(mutable_list)