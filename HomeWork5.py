#Задание 1.Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


my_file = open('HW5_1.txt', 'w')
my_line = input('Введите текст:  \n')
while my_line:
    my_file.writelines(my_line)
    my_line = input('Введите текст:  \n')
    if not my_line:
        break

my_file.close()
my_file = open('HW5_1.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()



# Задание 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


my_file = open('HW5_2.txt', 'r')
file_content = my_file.read()
print(f'Содержимое файла: \n {file_content}')
my_file = open('HW5_2.txt', 'r')
file_content = my_file.readlines()
print(f'Количество строк в файле: {len(file_content)}')
my_file = open('HW5_2.txt', 'r')
file_content = my_file.readlines()
for i in range(len(file_content)):
    print(f'Общее количество символов {i + 1}-ой строки: {len(file_content[i])}')

my_file = open('HW5_2.txt', 'r')
file_content = my_file.read()
file_content = file_content.split()
print(f'Общее количество слов: {len(file_content)}')
my_file.close()



#Задание 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open('HW5_3.txt', 'r') as my_file:
    salary = []
    small_salary = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            small_salary.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 у сотрудника {small_salary}, средняя величина дохода сотрудников {sum(map(int, salary)) / len(salary)}')



# Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


my_voc = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('HW5_4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(my_voc[i[0]] + ' ' + i[1])
    print(new_file)

with open('HW5_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)



# Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def my_summary():
    try:
        with open('HW5_5.txt', 'w+') as file_object:
            line = input('Введите цифры через пробел: \n')
            file_object.writelines(line)
            my_number = line.split()

            print(sum(map(int, my_number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода данных')


my_summary()



# Задание 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# !!!Тут важно знать, что нужно указывать все данные, раз это все таки словарь и вместо отсутствующего значения прописывать в тексте файла нули!!!


lessons = {}
with open('HW5_6.txt', 'r') as lessons_count:
    for line in lessons_count:
        subject, lectures, practice, labs = line.split()
        lessons[subject] = int(lectures) + int(practice) + int(labs)
    print(f'Common count of hours of subjects: \n {lessons}')



# Задание 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.........


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