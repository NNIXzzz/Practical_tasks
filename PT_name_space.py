#Домашняя работа по уроку "Пространство имён"

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(your_word):
    tuple_your_word = tuple((len(your_word), your_word.upper(), your_word.lower()))
    print(tuple_your_word)
    count_calls()

def is_contains(your_word, list_to_search):
    if your_word.lower() in (word.lower() for word in list_to_search):
        print(True)
    else:
        print(False)
    count_calls()



string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)

