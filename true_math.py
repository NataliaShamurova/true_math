from math import inf
def divide(a, b):
    res = 0
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        res = inf
        return inf

# Вводим значения
first = float(input())
second = float(input())

result = divide(first, second)
print(result)
