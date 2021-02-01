# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random as r
from timeit import timeit
from cProfile import run


def min_max_1(arr_, idx={'minimum': 0, 'maximum': 0}):
    for i, item in enumerate(arr_):  # пробегаем один раз по массиву и находим индексы max и min
        if item < arr_[idx['minimum']]:
            idx['minimum'] = i
        elif item > arr_[idx['maximum']]:
            idx['maximum'] = i
    arr_[idx['minimum']], arr_[idx['maximum']] = arr_[idx['maximum']], arr_[idx['minimum']]
    return arr  # меняем местами


def min_max_2(arr_):
    min_ = arr_.index(min(arr_))  # индекс минимального числа
    max_ = arr_.index(max(arr_))  # индекс максимального числа
    arr_[min_], arr_[max_] = arr_[max_], arr_[min_]
    return arr_


def min_max_3(arr_, idx={'minimum': 0, 'maximum': 0}):
    for i, item in enumerate(arr_):  # пробегаем один раз по массиву и находим индексы max и min
        if item < arr_[idx['minimum']]:
            idx['minimum'] = i
    for i, item in enumerate(arr_):  # пробегаем один раз по массиву и находим индексы max и min
        if item < arr_[idx['maximum']]:
            idx['maximum'] = i

    arr_[idx['minimum']], arr_[idx['maximum']] = arr_[idx['maximum']], arr_[idx['minimum']]
    return arr_  # меняем местами


SIZE = 10000
MIN_ITEM = 0
MAX_ITEM = 999
arr = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

start_ = 100_000
end_ = 500_000
step_ = start_

for i in range(start_, end_ + 1, step_):
    arr1 = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(i)]
    print(f'min_max_1 size {i} = {timeit("min_max_1(arr1)", number=100, globals=globals())}')

print(run('min_max_1(arr)'))

for i in range(start_, end_ + 1, step_):
    arr1 = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(i)]
    print(f'min_max_2 size {i} = {timeit("min_max_2(arr1)", number=100, globals=globals())}')

print(run('min_max_2(arr)'))

for i in range(start_, end_ + 1, step_):
    arr1 = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(i)]
    print(f'min_max_3 size {i} = {timeit("min_max_3(arr1)", number=100, globals=globals())}')

print(run('min_max_3(arr)'))

# min_max_1 - ручной поиск индексов за 1 проход О(n)
# min_max_1 size 100000 = 2.416158963
# min_max_1 size 200000 = 4.450866736
# min_max_1 size 300000 = 6.577148612000001
# min_max_1 size 400000 = 8.742862144999998
# min_max_1 size 500000 = 11.609795502999997

# min_max_2 - поиск максимального и минимального число с использованием функций min max О(2n)
# min_max_2 size 100000 = 0.4862260559999996
# min_max_2 size 200000 = 0.9558037090000013
# min_max_2 size 300000 = 1.456604855000002
# min_max_2 size 400000 = 1.9302604259999967
# min_max_2 size 500000 = 2.3820096259999985

# min_max_3 - ручной поиск индексов за 2 прохода О(2n)
# min_max_3 size 100000 = 2.6225472479999965
# min_max_3 size 200000 = 4.929998861999998
# min_max_3 size 300000 = 7.568544164999999
# min_max_3 size 400000 = 10.171872925999992
# min_max_3 size 500000 = 12.366552569999996

# min_max_1
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les4_task1.py:7(min_max_1)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# min_max_2
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les4_task1.py:17(min_max_2)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# min_max_3
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les4_task1.py:24(min_max_3)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: несмотря на то, что в min_max_2 поиск минимального и максимального осуществляется через 2 прохода массива
# всеже компилятор справляется с этой задачей быстрее (время выполнения во всех случаях увеличивается линейно)
