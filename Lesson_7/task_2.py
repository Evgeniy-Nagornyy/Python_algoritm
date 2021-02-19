# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def sort_connect(arr):
    if len(arr) <= 1:
        return arr

    arr_1 = sort_connect(arr[:len(arr) // 2])
    arr_2 = sort_connect(arr[len(arr) // 2:])
    i = 0
    j = 0

    while len(arr_1) > i and len(arr_2) > j:
        if arr_1[i] < arr_2[j]:
            arr[i + j] = arr_1[i]
            i += 1
        else:
            arr[i + j] = arr_2[j]
            j += 1

    while len(arr_1) > i:
        arr[i + j] = arr_1[i]
        i += 1
    while len(arr_2) > j:
        arr[i + j] = arr_2[j]
        j += 1

    return arr


array = [random.uniform(0, 50) for _ in range(10)]
print(array)
print(sort_connect(array))