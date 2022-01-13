separator = '<<<<<-------------------->>>>>'

# if

cars = ['bmw', 'audi', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Проверка по нескольким условиям
car = 'toyota'

if car == 'toyota' and car != 'bmw':
    print(f'Это же {car}!')

if car != 'bmv' or car != 'audi':
    print('Моя бибика!')

# Проверка нескольких вариантов
age = 99
name = 'Andy'

if age >= 18 and age < 80:
    print(f'Заходи, {name}')
elif age >= 80:
    print('Проваливай, дедуля!')
else:
    print('Убираяся мелкосопочник!')

print(separator)

# Проверка списков

# Проверка наличия в списке
print(f'проверка bmw в списке: {"bmw" in cars}')

# Проверка отсутствия в списке
print(f'Нет моего Datsun среди машин: {"datsun" not in cars}')

# Простая проверка на пустоту списка
toppings = []

if toppings:
    for top in toppings:
        print(top)
else:
    print('Empty toppings')
