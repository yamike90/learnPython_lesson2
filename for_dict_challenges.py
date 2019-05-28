# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

#students = ['Вася', 'Петя', 'Маша', 'Маша', 'Петя']


students_list = list(d['first_name'] for d in students) #преобразование словаря в список значений словаря
frequency = {} #пустой список, где key = Имя ученика, value = количество повторений в последовательности
for student in students_list:
    frequency[student] = students_list.count(student) 

for freq_key, freq_value in frequency.items(): #перебор key и value в словаре для последовательного вывода
    print('{} : {}'.format(freq_key, freq_value))

#подсмотренное в чате решение
for i in set(name['first_name'] for name in students):
  print("{}: {}".format(i, students.count({"first_name": i})))
   


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

students_list = list(d['first_name'] for d in students) #преобразование в список
most_frequent_name = max(set(students_list), key=students_list.count) #понять как работе key. поиск самого повторябщегося через преобразование в множество
print(f'Самое частое имя среди учеников: {most_frequent_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]


# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


for class_number, students_list in enumerate(school_students, start=1):  #class_number - номер класса
    students_list = list(d['first_name'] for d in students_list) #students_list - преобразованный в список словарь для каждого отдельного класса
    most_frequent_name = max(set(students_list), key=students_list.count) #поиск самого частого имени для каждого класса
    print(f'Самое частое имя в классе {class_number}: {most_frequent_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


for class_dict in school: #перебор классов
    class_names_dict_listed = list(class_dict['students']) #список словарей с именами для каждого класса
    class_names_list = list(d['first_name'] for d in class_names_dict_listed) #список имен для каждого класса

    class_sex_male_count = 0 #счетчик мальчиков
    class_sex_female_count = 0 #счетчик девочек
    for student in class_names_list: #перебор имен для каждого класса
        if is_male[student]:
            class_sex_male_count += 1
        else:
            class_sex_female_count += 1
    class_number = class_dict['class'] #сохраняем название класса для каждой итерации (можно было сделать сразу в выводе)
    print(f'В классе {class_number} {class_sex_female_count} девочки и {class_sex_male_count} мальчика.')
    



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

max_girls = 0
max_boys = 0
for class_dict in school: #перебор классов
    class_names_dict_listed = list(class_dict['students']) #список словарей с именами для каждого класса
    class_names_list = list(d['first_name'] for d in class_names_dict_listed) #список имен для каждого класса

    class_sex_male_count = 0 #счетчик мальчиков
    class_sex_female_count = 0 #счетчик девочек
    for student in class_names_list: #перебор имен для каждого класса
        if is_male[student]:
            class_sex_male_count += 1
        else:
            class_sex_female_count += 1

    if class_sex_male_count > max_boys:
        max_boys = class_sex_male_count
        class_boys = class_dict['class']
    if class_sex_female_count > max_girls:
        max_girls = class_sex_female_count
        class_girls = class_dict['class']

print(f'Больше всего мальчиков в классе {class_boys}')
print(f'Больше всего девочек в классе {class_girls}')
    