text = "Это текст со знаками препинания: точка, запятая и двоеточие."

for char in ',.!?:':
    text = text.replace(char, '')

word_tuple = tuple(text.split())

print(word_tuple)
