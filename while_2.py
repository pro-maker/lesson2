# Функция с while-диалогом

# Словарь диалогов
dialog = {
    "Как дела?": "Хорошо!", 
    "Что делаешь?": "Программирую",
    "Что дальше?": "Буду много программировать",
    "И как быть?": "Учить Python, а не дурака валять!"    
}


# Дятел
def ask_user(dlg):
    while True:
        # Вопрос пользователя
        print('Вопрос пользователя: ')
        ask = input()
        # Ответ программы
        print('Ответ программы: ')
        for ask_dlg in dlg:
            if ask_dlg == ask:
                print(dlg[ask_dlg])

ask_user(dialog)
