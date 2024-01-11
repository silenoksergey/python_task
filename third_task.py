# 3
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.


surname = input('Enter your surname: ')
age = int(input('Enter your age: '))
weight = int(input('Enter your weight: '))

if age < 30 and (weight >= 50 or weight < 120): # не понял, почему не работал вариант: age < 30 and 50 >= weight < 120
    print(f"{surname}, {age} years old, weight {weight}, good condition")

elif age > 40 and (weight < 50 or weight > 120):
    print(f"{surname}, {age} years old, weight {weight}, medical examination is required!")

elif age > 30 and (weight < 50 or weight > 120):
    print(f"{surname}, {age} years old, weight {weight}, you should take care of yourself") # 30 лет включаем в этот диапазон? сейчас 30 лет не входит никуда

else:
    print(f"{surname}, {age} years old, we are awesome")
