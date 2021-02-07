from sys import getsizeof, version, platform
from random import randint as r

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 999
arr = [r(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
idx = {'minimum': 0, 'maximum': 0}

for i, item in enumerate(arr):  # пробегаем один раз по массиву и находим индексы max и min
    if item < arr[idx['minimum']]:
        idx['minimum'] = i
    elif item > arr[idx['maximum']]:
        idx['maximum'] = i
arr[idx['minimum']], arr[idx['maximum']] = arr[idx['maximum']], arr[idx['minimum']]

size1 = getsizeof(SIZE) + getsizeof(MAX_ITEM) + getsizeof(MIN_ITEM) + getsizeof(arr) + \
        getsizeof(idx) + getsizeof(i) + getsizeof(item)
for i in arr:  # добавляем объем переменных в массиве
    size1 += getsizeof(i)
print(f'Объем памяти в первом варианте - {size1}')

#  ----------------------------------------------------------------------------------------

min_ = arr.index(min(arr))  # индекс минимального числа
max_ = arr.index(max(arr))  # индекс максимального числа
arr[min_], arr[max_] = arr[max_], arr[min_]

size2 = getsizeof(SIZE) + getsizeof(MAX_ITEM) + getsizeof(MIN_ITEM) + getsizeof(arr) \
        + getsizeof(min_) + getsizeof(max_)
for i in arr:  # добавляем объем переменных в массиве
    size2 += getsizeof(i)
print(f'Объем памяти во втором варианте - {size2}')

#  ----------------------------------------------------------------------------------------


for i, item in enumerate(arr):  # пробегаем один раз по массиву и находим индексы max и min
    if item < arr[idx['minimum']]:
        idx['minimum'] = i
for i, item in enumerate(arr):  # пробегаем один раз по массиву и находим индексы max и min
    if item < arr[idx['maximum']]:
        idx['maximum'] = i

arr[idx['minimum']], arr[idx['maximum']] = arr[idx['maximum']], arr[idx['minimum']]

size3 = getsizeof(SIZE) + getsizeof(MAX_ITEM) + getsizeof(MIN_ITEM) + getsizeof(arr) + \
        getsizeof(idx) + getsizeof(i) + getsizeof(item)
for i in arr:  # добавляем объем переменных в массиве
    size3 += getsizeof(i)
print(f'Объем памяти в третьем варианте - {size3}')
print(f'Версия Python - {version}\nПлатформа - {platform}\nРазрядность - Х86_64')

#  ----------------------------------------------------------------------------------------
# Объем памяти в первом варианте - 37380
# Объем памяти во втором варианте - 37148
# Объем памяти в третьем варианте - 37380
# Вывод: второй вариан занимает меньше памяти так как в нем отсутствует словарь idx
#        третий вариант занимает столько же памати, сколько и первый так как количество переменных одинаково
# Версия Python - 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34)
# [Clang 6.0 (clang-600.0.57)]
# Платформа - darwin
# Разрядность - Х86_64
