separator = '*************************'

# Объявление списка
bicycles = ['merida', 'cube', 'trek', 'giant', 'gt', 'pinarello']

print(f'Список велосов: {bicycles}')
print(f'Велос по индексу 0: {bicycles[0].title()}')

# Обращение через отрицательный индекс ищет элемент с конца
print(f'Велос по индексу -1: {bicycles[-1].title()}')

print(separator)

# Редактирование элемента списка
bicycles[-1] = 'cannondale'

print(f'Изменили последний элемент списка: {bicycles}')

# Добавление нового элемента списка
bicycles.append('bmc')

print(f'Добавили новый велос: {bicycles}')

# Вставка на определённую позицию нового элемента
bicycles.insert(2, 'specialized')
print(f'Вставка нового велоса: {bicycles}')

# Удаление безследно из списка со сдвигом элементов
del bicycles[-1]

print(f'Грохнули один велос: {bicycles}')

# Удаление и возвращение элемента из списка со сдвиком элементов. Без параметра удаляет последний элемент списка
old_bicycle = bicycles.pop(-2)

print(f'Удалили велос {old_bicycle.title()} из списка. Осталось: {bicycles}')

# Удаление элемента по значению без возврата значения
other_bicycle = 'cannondale'
bicycles.remove(other_bicycle)

print(f'Удалили ещё один велос: {other_bicycle} осталось: {bicycles}')

print(separator)

# Упорядочение списка

# Сортировка списка
bicycles.sort()

print(f'Список отсортирован: {bicycles}')

# Сортировка списка в обратном порядке
bicycles.sort(reverse=True)

print(f'Список отсортирован наоборот: {bicycles}')

# Сортировка списка с сохранием текущего без изменеий
new_list = sorted(bicycles)

print(f'Текущий список: {bicycles} Отсортированный список {new_list}')

# Переворачивание списка в обратном порядке
cars = ['toyota', 'bmv', 'lada', 'reno', 'audi']

print(f'Исходный список: {cars}')

cars.reverse()

print(f'Перевёрнутый список: {cars}')

print(separator)

# Длинна списка
print(f'Всего велосов: {len(bicycles)}, а бибик: {len(cars)}')

print(separator)

# Работа со списками

# Перебор списка
bicycles_string = ''

for bike in bicycles:
  bicycles_string += f'{bike.title()}; '

print(f'Список велосов форматированный: {bicycles_string}')

print(separator)

# Создание числовых списков

numbers = range(1, 10)
numbers_sting = ''

print(f'Range не трансформируется в последовательность чисел: {numbers}')
print(f'Чтобы привести range к списоку нужно его прописочить через list: {list(numbers)}')

for num in numbers:
  numbers_sting += f'{num}; '

print(f'Числа из range не включают последнее число: {numbers_sting}')

# уквзвние шага в range
print(f'Проба шага для range: {list(range(1, 21, 2))}')

print(f'Минимум из списка {list(numbers)} = {min(list(numbers))}')
print(f'Максимум из списка {list(numbers)} = {max(list(numbers))}')
print(f'Сумма списка {list(numbers)} = {sum(list(numbers))}')

# Создание списка через герератор
numbers = [value**2 for value in range(1, 10)]

print(f'Построение списка через генератор: {numbers}')

print(separator)


# Работа с частью списка

heroes = ['batman', 'super man', 'spider man', 'super andy', 'candy candy', 'iron man']

print(f'Выборка части списка: {heroes[1:4]}')
print(f'Если не указывать начало и/или конец среза то вывод будет либо начинаться с 0-го элемента либо заканчиваться -1 элементом последователности:\n{heroes[:]}')
print(f'Третий параметр среза отвечает за шаг выборки: {heroes[:5:2]}')

# Копирование списка
default_list = list(range(1, 20))

default_list.append(1)

new_list = default_list[:]

print(f'Копировать список можно через срез: {new_list}')

