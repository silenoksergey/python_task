# 1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.


import json, pickle

my_favourite_group = {
    "name": "Г.М.О.",
    "tracks": ["Последний месяц осени", "Шапито"],
    "Albums": [
        {"name": "Делать панк-рок", "year": 2016},
        {"name": "Шапито", "year": 2014}
    ]
}
group_json = json.dumps(my_favourite_group)
print(f"Сериализация в json: {group_json}")

group_pickle = pickle.dumps(my_favourite_group)
print(f"Сериализация в pickle: {group_pickle}")


with open('group.json', 'w', encoding="utf-8") as files:
    files.write(json.dumps(my_favourite_group)) # создание файла group.json и запись в него сериализованого значения

with open('group.pickle', 'wb') as files:
    files.write(pickle.dumps(my_favourite_group)) # создание файла group.pickle и запись в него сериализованого значения