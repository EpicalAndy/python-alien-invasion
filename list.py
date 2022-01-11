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
