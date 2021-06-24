import json


my_voc_1 = {}
my_voc_2 = {}
profits = 0
average_profit = 0
i = 0
with open('HW5_7.txt', 'r') as file:
    for line in file:
        name, company_type, profit, damages = line.split()
        my_voc_1[name] = int(profit) - int(damages)
        if my_voc_1.setdefault(name) >= 0:
            profits = profits + my_voc_1.setdefault(name)
            i += 1
    if i != 0:
        average_profit = profits / i
        print(f'Средняя прибыль составляет: {average_profit:.2f}')
    else:
        print(f'Средняя прибыль отсутствует. Все  работают в убыток')
    my_voc_2 = {'средняя прибыль': round(average_profit)}
    my_voc_1.update(my_voc_2)
    print(f'Прибыль каждой компании - {my_voc_1}')

with open('HW5_7.json', 'w') as write_js:
    json.dump(my_voc_1, write_js)

    js_str = json.dumps(my_voc_1)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}') 