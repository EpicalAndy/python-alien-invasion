separator = '======================================='


# Пример функции
def hi():
    '''Тупо печатает тебе приветики!!!'''
    print('Hi, person!')


hi()

print(separator)


# Параметры функции

# Определение параметра
def hi_person(name):
    print(f'Hi, {name}!')


hi_person('Andy')


# Позиционные аргументы
def hi_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')


hi_user('Andy', 'Ubi')
hi_user('Kris', 'Jericho')

# Именнованные аргументы
hi_user(first_name='Antonio', last_name='Banderas')


# Значение аргументов по умолчанию. AХТУНГ параметры со значением по умолчанию должны расологатся в конце объявления функции
def print_person_data(age, name='empty', gender='middle'):
    print(f'Name: {name.title()}, age: {age}, gender: {gender}')


print_person_data(22)

print(separator)

# Возвращение значений из функци

# Возвращение простого значения
value = '0.0'


def get_modified_data(val):
    ''' Оборачивает значение усами '''
    return f'-= {val} =-'


print(f'Модифицируем {value} в это: {get_modified_data(value)}')

# Пример использования функции
user_list = [
    {'first_name': 'jon', 'last_name': 'coner', 'age': 20},
    {'first_name': 'mike', 'last_name': 'tison', 'age': 20},
    {'first_name': 'dead', 'last_name': 'mazay', 'age': 20}
]


def print_full_user_data(first_name, last_name, second_name='', age=None):
    ''' Печатает информацию о пользователе '''
    print(f'User {first_name} {last_name} {second_name} age {age}')


for user in user_list:
    print_full_user_data(user['first_name'].title(), user['last_name'].title(), user['age'])


# Передача произвольных позиционных аргументов в функцию. Сам параметру в итоге будет представлять из себя кортеж (tuple)
def print_user_names(*names):
    print(f'Печать произвольного списка имён: {names}')


print_user_names('Даша', 'Петя', 'Жора')


# Произвольный аргумент должен быть один и стоять в самом конце списка параметров
def print_students_data(group, *students):
    print(f'Группа: {group}; студенты: {students}')


print_students_data('ГГ99', 'Даша', 'Петя', 'Жора')


# Произволный набор именнованных параметров. Внутри функции такой параметр представляет собой словарь
def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info


user_profile = build_profile('Andy', 'Ubi', location='Moscow', phone='Nokia')

print(user_profile)
