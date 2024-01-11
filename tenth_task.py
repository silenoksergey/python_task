# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name- строка полученная от пользователя,
# health= 100,
# damage= 50.  Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию  attack(person1, person2).
# Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.

name_player = input("Введите имя игрока: ")
enemy_player = input("Введите имя противника: ")
player = {"name": name_player, "health": 100, "damage": 50, "armor": 1.2}
enemy = {"name": enemy_player, "health": 80, "damage": 40, "armor": 1.2}

def attack(*, person1=player, person2=enemy):

    def damage_received(armor=person1, damage=person2):  #наносим урон
        result_damage = damage["damage"] / armor["armor"]
        return result_damage

    action_damage = person1["health"] - damage_received() #считаем урон за вычетом брони

    return action_damage

print(attack(person1=player, person2=enemy))

