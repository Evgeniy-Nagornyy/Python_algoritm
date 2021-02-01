# Определить, какое число в массиве встречается чаще всего.
import random as r

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 2
array = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
num_count = [None, 0]  # номер и его количество в массиве

print(array)

for i in array:
    if array.count(i) > num_count[1]:
        num_count = [i, array.count(i)]

print(f'число {num_count[0]} встречается чаще всего: {num_count[1]} раз')
