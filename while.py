separator = '--==================================--'

# while
current_number = 0
numbers_string = ''

while current_number <= 5:
    numbers_string += str(current_number) + '; '
    current_number += 1

print(f'Получили следующие числа: {numbers_string}')

# Выход из цикла управляется пользователем
prompt = 'Вееди что нибудь что бы продолжить либо q для выхода: '
message = ''

while message.lower() != 'q':
    message = input(prompt)

    print(f'Чел, ты ввёл это: {message}')

print(f'Дасвидос чувак, ты ввёл: {message}')

print(separator)

# Выход из цикла с помощью break
exit_char = 'quit'
prompt = f'Вееди что нибудь что бы продолжить либо {exit_char} для выхода: '
message = ''

while message.lower() != exit_char:
    message = input(prompt)

    if message.lower() == exit_char:
        break

    print(f'Чел, ты ввёл это: {message}')

print(f'Дасвидос чувак, ты ввёл: {message}')

print(separator)

# Остановка текущей итерации через continue и переход к следующей
exit_char = 'quit'
break_char = 'break'
prompt = f'Вееди что нибудь что бы продолжить либо {exit_char} для выхода или {break_char} что бы начать сначало: '
message = ''

while message.lower() != exit_char:
    message = input(prompt)

    if message.lower() == break_char:
        continue

    if message.lower() == exit_char:
        break

    print(f'Чел, ты ввёл это: {message}')

print(f'Дасвидос чувак, ты ввёл: {message}')

print(separator)

# Работа со списками
registered_users = ['andy', 'candy', 'jon', 'lolita', 'admin']
new_users = ['Andy', 'Mike', 'Colobok']
new_users_count = len(new_users)
new_user = ''

print(f'Текущий список пользователей: {registered_users}')
print(f'Список новых пользователей: {new_users}')

while new_users_count:
    new_users_count -= 1
    new_user = new_users[new_users_count].lower()

    if new_user in registered_users:
        print(f'Опа! А пользователь {new_user} уже зарегистрирован в системе')
        continue

    registered_users.append(new_user)

print(f'Теперь список зарегистрированных пользователей таков: {registered_users}')

print(separator)

# While с использованием in
pets = ['dog', 'cat', 'dog', 'cat', 'rabbit']

print(f'Вся живность: {pets}')

while 'cat' in pets:
    pets.remove('cat')

print(f'Tеперь список живности такой: {pets}')
