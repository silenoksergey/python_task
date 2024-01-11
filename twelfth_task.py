# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random

def list_not_null(*, list):
    if len(list) != 0:
        random_list = random.choice(list)
        return random_list
    else:
        return None

input_list = [1,2,3,4]

print(list_not_null(list=input_list))

