# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random as r

SIZE = 10
MIN_ITEM = -1
MAX_ITEM = 2
array = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
maximum = [MIN_ITEM - 1, '_']
print(array)

for i, item in enumerate(array):
    if 0 > item > maximum[0]:
        maximum = [item, i]

if maximum[0] == '_':  # проверяем изменила ли программа наш псевдо максимум
    print('в массиве отсутствуют отрицательные числа')
else:
    print(f'максимальное отрицательное число: {maximum[0]} с индексом: {maximum[1]}')
