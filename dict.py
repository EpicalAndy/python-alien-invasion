separator = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'

# Объявление словаря
jon = {'gender': 'man', 'age': 20, 'hands': 2, 'legs': 2, 'name': 'jon'}

# Через фигурные скобки также определяется множестов. Множество это тупо список значений {'jon', 1, True}
# без определённого порядка

print(f'Содержимое словаря: {jon}')

# Обратиться к свойству словаря
print(f'Имя человека: {jon["name"].title()}')

# Добавить свойство к словарю
jon['color'] = 'white'

print(f'Теперь словрь выглядит так: {jon}')

# Удаление элемента словаря
del jon['color']

print(f'После удаления имеем такой словарь: {jon}')

# Получить все ключи словаря
print(f'Все ключи словаря и получить список: {list(jon.keys())}')

# Получение значения через метод get
print(f'Если get не может найти свойство, то он вернёт то что передали во второй параметр: {jon.get("color", "What?")}')
print(f'Если в get 2 параметр не передан и свойства не существует вернётся None: {jon.get("color")}')

print(separator)

# Перебор словаря

# for in
dict_string = ''

for key, value in jon.items():
    dict_string += f'для {key} значение {value}; '

print(f'Словарь в строку: {dict_string}')

# Перебор только ключей
keys_string = ''

for key in jon.keys():
    keys_string += f'{key}; '

print(f'Список ключей: {keys_string}')

# Перебор по отсортированным ключам
sorted_keys_list = list(sorted(jon.keys()))
sorted_keys_string = ''


for key in sorted_keys_list:
    sorted_keys_string += f'{key}; '

print(f'Отсортированные ключи: {sorted_keys_string}')

# Перебор значений
values_list = list(jon.values())
values_string = ''

for value in values_list:
    values_string += f'{value}; '

print(f'Все значения словаря строкой: {values_string}')

# Через set() можно получить уникаьные значения словаря
print(f'Уникальные значения словаря: {set(values_list)}')
