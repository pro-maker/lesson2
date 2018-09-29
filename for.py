
# Строка

str1 = input('String: ')
for symbol in str1:
    print(symbol)

print('\n--\n')

# Список

students_scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for score in students_scores:
    print(score+1)

print('\n--\n')

# Список со словарями

# phones = {'iPhone': 'XS', 'Samsung': 'Galaxy Note 9', 'Xiaomi': 'Mi7'}
# Перебор ключей по словарю
# for key in phones:
#   print ('{} -> {}'.format(key, phones[key]))

# Структрура:
# Список_классов = [
#   Словарь_оценок_по_классам
#   ]

dic_school = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [3,5,2]},
    {'school_class': '4c', 'scores': [5,4,3,2,3,4,5]},
    ]

# Перебор классов в списке школы
j = 0 # счетчик количества оценок в школе
school_summ = 0
for sch_class in dic_school:
    # Перебор оценок по классам 
    i = 0 # счетчик количества оценок в классе
    class_summ = 0
    for class_scores in sch_class['scores']: 
        i += 1
        class_summ += class_scores
        j += 1
        school_summ += class_scores
    # Средний балл по классу
    print('Класс ' + sch_class['school_class'] + ': ' + "{:,.2f}".format(class_summ/i))
# Средний балл по школе
print('Средний балл по школе: ' + "{:,.2f}".format(school_summ/j))

