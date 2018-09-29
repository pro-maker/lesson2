def str_compare(str1, str2):
    # 0. Тип "Строка"
    if (isinstance(str1, str) and isinstance(str2, str)):
        # 1. Одинаковые строки
        if (str1 == str2): return 1
        else:
            # 2. Длина строк
            if (len(str1) > len(str2)): return 2
            # 3. Вторая строка 'learn'
            elif (str2 == 'learn'): return 3
            # 4. Выход из батареи условий
            else: return "The end"
    else: return 0

# 0. Тип "Строка"
a = 1
b = 'bbb'
c = str_compare(a, b)
print('{}: Тип "Строка" ("{}" / "{}")'.format(c, a, b))

# 1. Одинаковые строки
a = 'aaa'
b = 'aaa'
c = str_compare(a, b)
print('{}: Тип "Строка" ("{}" / "{}")'.format(c, a, b))

# 2. Длина строк
a = 'aaa'
b = 'aa'
c = str_compare(a, b)
print('{}: Тип "Строка" ("{}" / "{}")'.format(c, a, b))

# 3. Вторая строка 'learn'
a = 'aaa'
b = 'learn'
c = str_compare(a, b)
print('{}: Тип "Строка" ("{}" / "{}")'.format(c, a, b))

# 4. Выход из батареи условий
a = 'aaa'
b = 'aaaa'
c = str_compare(a, b)
print('{}: Тип "Строка" ("{}" / "{}")'.format(c, a, b))
