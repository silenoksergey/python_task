# Тема: встроенные типы и операции с ними
# 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
# Примечание. Списки создайте вручную, например так: my_list_1 = [2, 5, 8, 2, 12, 12, 4] my_list_2 = [2, 7, 12, 3]

my_list1 = [2, 5, 8, 2, 12, 12, 4]
my_list2 = [2, 7, 12, 3]
result_list = []

for i in my_list1:
    if i not in my_list2:
        result_list.append(i)

print(result_list)












