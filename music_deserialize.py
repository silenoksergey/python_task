# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.
import json, pickle

with open ('group.json', 'r') as read_file:
    group_json = json.load(read_file)
print(group_json)

with open ('group.pickle', 'rb') as read_file:
    group_pickle = pickle.load(read_file)
print(group_pickle)