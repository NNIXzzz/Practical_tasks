#Домашнее задание по теме "Оператор "with"

import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower()
                        line = re.sub(r'[,.=\?!:; -]', ' ', line)
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            try:
                position = words.index(word)
                result[file_name] = position
            except ValueError:
                pass
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result

finder2 = WordsFinder('test_file.txt')

with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("It's a text for task Найти везде,\n")
    f.write("Используйте его для самопроверки.\n")
    f.write("Успехов в решении задачи!\n")
    f.write("text text text\n")

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
