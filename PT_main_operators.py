#Дополнительное практическое задание по модулю: "Основные операторы"

import random

n = random.randint(3, 20)

found_pairs = []

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        insert = i + j
        if n % insert == 0:
            found_pairs.append((i, j))

output_string = "".join("".join(map(str, i)) for i in found_pairs)

print(f'{n} - {output_string}')