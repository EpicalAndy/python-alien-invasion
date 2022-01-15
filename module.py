# Импортирование всего модуля. Через as можно задать псевдоним
import function as f

# Обращение к элементу из модуля
f.hi()

# Импортирование функции и назначение ей псевдонима
from separator import print_separator as ps

ps()

# Ещё один вариант импорта
from sys import *

print(version)
