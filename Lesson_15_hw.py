import json

my_data = {}
while True:
    name = input('Input the name of goods: ')
    cost = int(input('Input the cost of goods: '))
    if name == 'stop':
        break
    else:
        dict_element = dict.fromkeys([name], cost)
        my_data.update(dict_element)
        print(my_data)

with open('data_hw.json', 'w', encoding='UTF-8') as file:  # запись в json файл
    json.dump(my_data, file, ensure_ascii=False)

with open('data_hw.json', encoding='UTF-8') as file:  # чтение из json файла
    data = json.load(file)
print(data)

data_values = data.values()   # подсчет стоимости покупок за день
res = 0
for n in data_values:
    res += n
print('Стоимость всех покупок за день равна:', res)


