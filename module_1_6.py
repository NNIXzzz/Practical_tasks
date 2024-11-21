#Практическое задание по теме: "Словари и множества"

#Словари

my_dict = {'Nikita': 2002, 'Vlad': 1994}

print(my_dict)

print(my_dict['Nikita'])
print(my_dict.get('Anatoli'))

my_dict.update({'Anjelika': 1974,
                'Agniya': 2002})

a = my_dict.pop('Nikita')
print(a)

print(my_dict)

#Множества

my_set = {1, 1, 'Nikita', 'Nikita', 12.34, 12.34}
print(my_set)

my_set.add(5)
my_set.add('Vlad')

my_set.discard(1)
print(my_set)