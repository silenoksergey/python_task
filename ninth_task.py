# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
def max_number(*, num1=int, num2=int) -> int:

    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2

    else:
        return num1


print(max_number(num1=3, num2=1))