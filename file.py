from separator import print_separator as ps
import datetime
import json

file_path = 'text_files/pi_shorts.txt'

# Запись содержимого файла в переменную
with open(file_path) as file:
    file_body = file.read()
# Почему-то переменную таким образом можно прочитать в не рамок with
print(file_body)

# Удаление переноса строки в конец файла. Не совсем понятно, делает это read() или print()
with open(file_path) as file:
    file_body_ = file.read()

print(file_body_.rstrip())

# Построчное чтение файла
with open(file_path) as file:
    for line in file:
        # Если нужно нужно убрать переносы строк то использовать эту строку
        # print(line.rstrip())
        print(line)

# Сохранение файла в переменную в виде списка строк
with open(file_path) as file:
    lines = file.readlines()

print(f'Список строк файла: {lines}')

ps()

# Капелька практики

# Поиск вхождения
file_path = 'text_files/pi_long.txt'
pi_string = ''

with open(file_path) as file:
    file_data = file.readlines()

    for line in file_data:
        pi_string += line.strip()

pi_string = pi_string.replace(' ', '')
birthday = input('Введите свой ДР в формате ддммгг: ')

if birthday in pi_string:
    print('Да детка!')
else:
    print(f'В строке {pi_string} нет даты {birthday}')

ps()

# Запись в файл

# Простая запись в файл. Если при записи файла нет то он будет создан
file_path = 'text_files/for_write.txt'
# encoding устанавливает кодировку для файла
with open(file_path, 'w', encoding='utf-8') as write_file:
    # По дефолту write() пишет в одну строку. Нжно самому добавлять разделители
    write_file.write('Вася шпилит Катю!\n')
    write_file.write('Жора шпилит Катю!!!')

# open() вторым параметром принимает следующие варианты: r - только чтение w - только запись a - добавление в файл
# r+ - чтение и запись

# Добавление данных к файлу
file_path = 'text_files/append_file'

with open(file_path, 'a', encoding='utf-8') as append_file:
    append_file.write(f'{datetime.date.today()}\n')

ps()

# Сохранение структурированных данных
file_path = 'text_files/data.json'


def write_json(file_path):
    numbers = [1, 2, 3, 4, 5]

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(numbers, f)


def load_json(file_path):
    with open(file_path) as f:
        numbers = json.load(f)

    print(f'Прочитали из {file_path} дааные: {numbers}')


write_json(file_path)
load_json(file_path)
