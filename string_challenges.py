# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
count_vowel = 0
for symbol in word:
    if symbol.lower() in ('у','е','ы','а','о','э','я','и','ю'): #можно создавать и использовать библиотеки для таких целей
        count_vowel += 1
print(count_vowel)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' '))) #split режет строку в список


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(' '):
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sum_all = 0
for word in sentence.split(' '):
    sum_all += len(word) #считаем общую длину всех слов
avg_word_len = sum_all / len(sentence.split(' ')) #делим общую длину всех слов на количество слов в приведенном списке
print(f'Усредненная длина слова: {avg_word_len}.')