# Домашнее задание
# Задача №1
# Ввод с клавиатуры. Если строка введённая с клавиатуры –
# это числа, то поделить первое на второе. Обработать
# ошибку деления на ноль. Если второе число 0, то
# программа запрашивает ввод чисел заново. Также если
# были введены буквы, то обработать исключение.


# Variant 1
while True:
    try:
        number1 = input('Input 1st number: ')
        number2 = input('Input 2nd number: ')
        result = int(number1) / int(number2)
        print(number1, '/', number2, '=', result)
    except ValueError:
        print('Error! Incorrect number is entered')
        continue
    except ZeroDivisionError:
        print('Error! Zero division')
        continue
    else:
        print('Program is complete')
        break

# Variant 2.
while True:
    try:
        key = input('Input "+" to continue or "stop" to exit the program: ')
        if key == 'stop':
            print('Program exit.')
            break
        elif key == '+':
            number1 = input('Input 1st number: ')
            number2 = input('Input 2nd number: ')
            result = int(number1) / int(number2)
            print(number1, '/', number2, '=', result)
        else:
            print('incorrect command is entered!')
    except ValueError:
        print('Error! Incorrect number is entered')
        continue
    except ZeroDivisionError:
        print('Error! Zero division')
        continue

