# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Cтрока – кол-во букв.
# Cделать проверку со всеми этими случаями.

a = (123, 225, 344, 'Python', 411, 589, 'hello', 'player', 646)
b = list(a)
c = 123454681187
d = 'Hello'


def data_type(data):
    if type(data) == tuple:
        len_of_words = 0
        for tuple_element in data:
            if type(tuple_element) == str:
                len_of_words += len(tuple_element)
        return print('Введен кортеж. Длина всех слов кортежа равна:', len_of_words, 'символов')
    elif type(data) == list:
        list_numbers_amt = 0
        list_letters_amt = 0
        for list_element in data:
            if type(list_element) == int:
                list_element = str(list_element)
                for number in list_element:
                    list_numbers_amt += len(number)
            elif type(list_element) == str:
                for word in list_element:
                    list_letters_amt += len(word)
        return print('Введен список. Количество чисел в списке:', ';',
                     list_numbers_amt, 'Количество букв в списке:', list_letters_amt)
    elif type(data) == int:
        odd_numbers = 0
        data = str(data)
        for int_element in data:
            int_element = int(int_element)
            if int_element % 2 == 0:
                odd_numbers += 1
        return print('Введено число. Количество нечетных чисел введенного числа:', odd_numbers)
    elif type(data) == str:
        num_of_letters = 0
        for str_element in data:
            num_of_letters += 1
        return print('Введена строка. Количество букв введенной строки:', num_of_letters)


data_type(b)
