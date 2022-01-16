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
