# x = 100 / 0

# try:
#     x = 100/0
# except ZeroDivisionError:
#     print('Вы делите на ноль')
#
# print('код дале...')
#
# try:
#     x = 100/0
# except ArithmeticError:
#     print('Вы делите на ноль')
#
# print('код дале...')

# d= {'name': 'fiodar'}
# try:
#     print(d['age'])
# except KeyError:
#     d['age'] = 1
# d1 = {'name': 'fiodar', 'age': 40}
# try:
#     v = d1['city']
# except KeyError:
#     print('index not found')
# except IndexError:
#     print('key not found')
# except Exception:
#     print('Big problem')
#
# try:
#     v = d1['city']
# except (IndexError, KeyError):  # не знаем какая отловлена ошибка
#     print('We have error')

# d1 = {'name': 'fiodar', 'age': 40}
# try:
#     v = d1['city']
#     print(v)
# except KeyError:
#     print('key not found')
# finally:
#     print('we have to da smth')

# d1 = {'name': 'fiodar', 'age': 40}
# try:
#     v = d1['city']
#     print(v)
# except KeyError:
#     print('key not found')
# else:
#     print('we have to da smth')

# Введите два числа с клавиатуры. Ȃоделите одно на другое.
# ȁбработайте ошибку деления на ноль, если ошибок нет, то результат
# деления возвести в квадрат. ȅакже используйте оператор finally.

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# try:
#     res = a / b
#     res = res ** 2
#     print(res)
# except ZeroDivisionError:
#     print('Деление на ноль')
# finally:
#     print('end of calculation')


# Введите два числа с клавиатуры. Ȃоделите одно на другое.
# ȁбработайте деления на ноль, преобразования и общее исключение.

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# try:
#     res = a / b
#     print(res)
# except TypeError:
#     print('Некорректный ввод')
# except ZeroDivisionError:
#     print('Деление на ноль')
# except Exception:
#     print('Ошибка')