# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
    print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
    print('Количестов букв в "{}": {}'.format(name, len(name)))


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
    if is_male[name]:
        sex = 'Мужской'
    else:
        sex = 'Женский'
    print('Пол "{}": {}.'.format(name, sex))


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего {len(groups)} группы.')
for group in groups:
    print(f'В группе {len(group)} ученика.')


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

for group_number, group in enumerate(groups, start=1): #перебор порядковых номеров и значений элементов списка
    print(f'Группа {group_number}: {", ".join(group)}') #join склеивает элементы последовательности в строку