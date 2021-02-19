# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
#     в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).
import random


def median(arr):
    for i in range(len(arr)):
        less = more = equally = 0
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                less += 1
            elif arr[i] > arr[j]:
                more += 1
            else:
                equally += 1
        equally -= 1
        if less == more or less == more + equally or more == less + equally or \
                (equally > 1 and abs(more - less) < equally):
            return arr[i]


array = [random.randint(0, 20) for _ in range(11)]
print(array)
print(f'num = {median(array)}')
print(sorted(array))
