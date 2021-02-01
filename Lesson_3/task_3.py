# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random as r

SIZE = 6
MIN_ITEM = 0
MAX_ITEM = 999
array = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
idx_ = {'minimum': 0, 'maximum': 0}  # индексы максимума и минимума

print(f'До: {array}')

for i, item in enumerate(array):  # пробегаем один раз по массиву и находим индексы max и min
    if item < array[idx_['minimum']]:
        idx_['minimum'] = i
    elif item > array[idx_['maximum']]:
        idx_['maximum'] = i

array[idx_['minimum']], array[idx_['maximum']] = array[idx_['maximum']], array[idx_['minimum']]  # меняем местами
print(f'После: {array}')
