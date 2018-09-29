# Забиваем на возможность кривого ввода
a = int(input("Age?"))

# Периодизация
def age_stage(age):
    if (age <= 3):
        return "Малыш"
    elif (age <= 6):
        return "Детский сад"
    elif (age <= 17):
        return "Школа"
    elif (age <= 22):
        return "ВУЗ"
    else:
        return "Кандидат в пенсионеры"

# Вывод
a = age_stage(a)
print (a)
