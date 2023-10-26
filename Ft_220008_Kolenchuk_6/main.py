count = int(input('Введите количество критериев:  '))
criteria = []
for i in range(count):
    criteria.append(input(f'Название критерия {i+1}:  '))

arr = []
for i in range(count):
    arr.append([])
    for j in range(count):
        arr[i].append([])

i = 0
j = 0
S = 0.0
sum_line = [0.0]*count
while i != count:
    while j != count:
        arr[i][j] = float(input(f'Относительная важность между критериями {criteria[i]} и {criteria[j]}:  '))
        sum_line[i] += arr[i][j]
        j += 1

    i += 1
    j = 0

    while j != i and i != count:
        arr[i][j] = round(1/(arr[j][i]), 2)
        sum_line[i] += round(arr[i][j], 2)
        j += 1

for el in sum_line:
    round(el, 2)
    S += el


weight_factor = []
for i in range(count):
    weight_factor.append(sum_line[i]/S)
    print(f'Весовой коэфф критерия {criteria[0]} равен {weight_factor[i]}')

print(arr)
print(sum_line)
print(S)
