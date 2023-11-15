# def my_f(*args, **kwargs):
#     print(args[2], type(args))
#     print(kwargs['name'], type(kwargs))
#
#
# my_f(0, 1, 2, name='Fiodar', age=39)

# def factorial(x):
#     if x != 0:
#         return x * factorial(x - 1)
#     else:
#         return 1
#
#
# print(factorial(5))
#
# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
#
# data = add(3, 4)
# print(data, type(data))
#
# def sq(x):
#     return x * x
#
#
# print(sq(2))
#
# square = sq
# print(square(3))

# def func_1(x):
#     def func_2(y):
#         return x * y
#
#     return func_2
#
#
# # print(func_1(2)(500))
#
# func_3 = func_1(5)
# print(func_3)

#
# def razr(x):
#     i = 0
#     while x > 0:
#         x = x // 10
#         i += 1
#     return i
#
#
# print(razr(265))

# import random
#
#
# def mas(a, b):
#     my_lst = [random.randint(a, b) for n in range(10)]
#
#
# mas(a=int(input('Введите a:')), b=int(input('Введите b:')))

# def timer(sec):
#     days = sec // (24 * 3600)
#     sec = sec % (24 * 3600)
#     hours = sec // 3600
#     sec = sec % 3600
#     minutes = sec // 60
#     sec = sec % 60
#
#     return f'{days}:{hours}:{minutes}:{sec}'
#
#
# print(timer(int(input('Введите время в секундах:'))))
#
#
# def letters(word):
#     glas = 0
#     sogl = 0
#     for i in word:
#         if i.isalpha() and i.lower() in 'aeiouy':
#             glas += 1
#         elif i.isalpha() and i.lower() in 'bcdfghjklmnpqrstvwxz':
#             sogl += 1
#     return print('Кол-во гласных:', glas,
#                  'Кол-во согласных:', sogl)
#
#
# letters(input('Введите слово: '))

# Задание №6
# Функцию которая при заданном целом числе n
# посчитает n + nn + nnn.
#
# def count(n):
#     nn = n * 2
#     nnn = n * 3
#     return int(n) + int(nn) + int(nnn)
#
#
# print('Результат n + nn + nnn:', count(input('Введите целое число n: ')))

# def func(x):
#     if -5 <= x <= 5:
#         return x * x
#     elif x < -5:
#         return 2 * abs(x) - 1
#     elif x > 5:
#         return 2 * x
#
#
# for i in range(-10, 11):
#     print(func(i), end=' ')



