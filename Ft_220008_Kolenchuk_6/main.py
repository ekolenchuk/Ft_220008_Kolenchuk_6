import sys

from tabulate import tabulate


def print_table(list_criteria, list_value, list_weight_factor):
    count_criteria = len(list_criteria)
    table = list_value.copy()
    for i in range(count_criteria):
        table[i].insert(0, list_criteria[i])
        table[i].append(list_weight_factor[i])
    list_criteria.insert(0, '')
    list_criteria.append('Весовой коэфф')
    table.insert(0, list_criteria)
    print(tabulate(table))


def round_sum(list):
    sum = 0.0
    for el in list:
        round(el, 2)
        sum += el
    return sum


try:
    count = int(input('Введите количество критериев:  '))
except ValueError:
    print("Oops! Неверный ввод!")
    sys.exit()
else:
    if count == 0 or count < 0:
        print("Oops! Неверный ввод! Нужно положительное целое число")
        sys.exit()

criteria = []
for i in range(count):
    criteria.append(input(f'Название критерия {i + 1}:  '))

arr = []

for i in range(count):
    arr.append([])
    for j in range(count):
        arr[i].append([])

i = 0
j = 0
sum_line = [0.0] * count
while i != count:
    while j != count:
        try:
            arr[i][j] = float(input(f'Относительная важность между критериями {criteria[i]} и {criteria[j]}:  '))
        except ValueError:
            print("Oops! Неверный ввод! Нужно положительное число в виде 0.00")
            continue
        if arr[i][j] < 0 or arr[i][j] == 0:
            print("Oops! Неверный ввод! Нужно положительное число в виде 0.00")
            continue

        sum_line[i] += arr[i][j]
        j += 1
    i += 1
    j = 0

    while j != i and i != count:
        arr[i][j] = round(1 / (arr[j][i]), 2)
        sum_line[i] += round(arr[i][j], 2)
        j += 1

sum_importance = round_sum(sum_line)

weight_factor = []
for i in range(count):
    factor = sum_line[i] / sum_importance
    weight_factor.append(round(factor, 2))
    # print(f'Весовой коэфф критерия {criteria[i]} равен {weight_factor[i]}')

print_table(criteria, arr, weight_factor)
