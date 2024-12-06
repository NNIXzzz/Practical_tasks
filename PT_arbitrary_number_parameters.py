#Самостоятельная работа по уроку "Произвольное число параметров"

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        i_lower = i.lower()
        root_word = root_word.lower()
        if root_word in i_lower or i_lower in root_word:
            same_words.append(i)
    return(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)