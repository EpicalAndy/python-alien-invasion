import separator


# Объявление класса
class Dog():
    # self всегда на первом месте!
    def __init__(self, name, age):
        ''' Инициалиция экземпляра '''
        self.name = name
        self.age = age

    def sit(self):
        ''' Команда сесть '''
        print(f'{self.name.title()} села!')


# Создание экземпляра класса
my_dog = Dog('Tima', 1)

# Вызов метода
my_dog.sit()

# Изменение состояния свойства
my_dog.name = 'Brulik'


class Car():
    def __init__(self, make, model, year):
        self.make = make or ''
        self.model = model or ''
        self.year = year or 0
        self.odometer = 0

    def print_car_description(self):
        print(
            f'Марка {self.make.title()} модель {self.model.title()} год производства {self.year} пробег {self.odometer}')

    def update_odometer(self, value):
        if value < self.odometer:
            print('Скручиваешь, стерлядь!?')
            return

        self.odometer = value

    def fill_gas(self):
        print(f'{self.make.title()} {self.model.title()} заправлена!')


subaru = Car('subaru', 'forester', 2015)
audi = Car('audi', 'tt', 2014)
datsun = Car('datsun', 'on-do', 2014)

datsun.fill_gas()

subaru.update_odometer(5)
subaru.print_car_description()
subaru.update_odometer(6)
subaru.print_car_description()
subaru.update_odometer(4)

subaru.print_car_description()

separator.print_separator()


# Наследование


# Класс который будет использован как свойство внутри класса Electro_car
class Battery():
    def __init__(self, battery_size=100):
        self.battery_size = battery_size

    def print_battery_description(self):
        print(f'Батарея на {self.battery_size} едениц')


# Класс который будет наслодоваться от родительского Car
class Electro_car(Car):
    def __init__(self, make, model, year):
        self.battery = Battery()

        super().__init__(make, model, year)

    # Переопределение родительского метода
    def fill_gas(self):
        print('Это электро тачка, чувак!')


tesla = Electro_car('tesla', 'model s', 2019)

tesla.print_car_description()
tesla.fill_gas()
tesla.battery.print_battery_description()
