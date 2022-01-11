separator = '-====================-'
words = 'hello string'

print(words.title())

words = 'Andrey Sotskov'

print(words.lower())
print(words.upper())

print(separator)

# ========== Постановка переменных в строку ===========

first_name = 'Andrey'
last_name = 'Sotskov'

print(f'{first_name} {last_name}')

first_name = 'andrey'
last_name = 'sotskov'

print(f'Hello {first_name.title()} {last_name.title()}!')

# Способ форматирования строки через f работает только с версии 3.6 раньше использовался метод строки формат
full_name = '{} {}'.format(first_name.title(), last_name.title())

print(separator)

# =============== Пробельные символы =====================

tab = '\tTab'
new_line = 'Next\nNew line'

print(f'{tab}\n{new_line}')

# Удаление лишних пробелов

long_string = ' Long string with whitespaces '

# Удалить справа
print(long_string.rstrip())

# Удалить слева
print(long_string.lstrip())

# Удалить с обоих концов
print(long_string.strip())
