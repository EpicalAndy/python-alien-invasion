import separator as sp

# Книжке которые можно юзать и которые не облагаются авторскими правами можно найти сдесь http://gutenberg.org
# Обработка ошибок с помощью try except
try:
    print(5/0)
except ZeroDivisionError:
    print('Ты с дуба рухнул? Чему тебя в школе учили, лаботряс!!!')

# Работа после срабатывания ошибки
print('Введи 2 числа! Я проверю!!!')
result = 0

while True:
    first_number = input('Первую вводи: ')

    if first_number.lower() == 'q':
        break

    second_number = input('Вторую вводи: ')
    if second_number == 'q':
        break

    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('По внимательнее, любезный!')

    if result > 0:
        print(f'Вот что получилось: {result}!')

        break

# Обработка отсутствия файла
file_path = 'unknow_file.txt'

try:
    with open(file_path, 'r') as unknown_file:
        print(unknown_file)
except FileNotFoundError:
    print(f'Опа! файла {file_path} нет!!!')

# Можно использовать оператор pass в качестве заглушки что бы тупо ничего не делать except
file_path = 'unknow_file.txt'

try:
    with open(file_path, 'r') as unknown_file:
        print(unknown_file)
except FileNotFoundError:
    pass
