s = input('Введите пароль: ')
result = 'Ваш пароль состоит только из цифр'

try:
    int(s)
except ValueError:
    result = 'Требования к паролю соблюдены'

try:
    1/len(s)
except ZeroDivisionError:
    result = 'Вы ввели пустой пароль'

print(result)

