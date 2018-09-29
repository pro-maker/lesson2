
# While-перебор с list.pop 
name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
while len(name_list):
    print(name_list.pop())

print('\n-------------\n')

# While-перебор с list.pop с проверкой вхождения строки
name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
while len(name_list):
    if (name_list.pop() == 'Валера'):
        print('Валера нашелся')
        break

print('\n-------------\n')

# While-диалог с остановкой по вводу строки
while True:
    user_say = input('Как дела? ')
    if user_say == 'Хорошо':
        print('Ну пока!')
        break
    else:
        print('Сам ты "{}"'.format(user_say))
