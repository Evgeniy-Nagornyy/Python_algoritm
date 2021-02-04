from timeit import timeit
from cProfile import run


def p_num(n):
    num = n
    b = []
    while len(b) < n:  # пока длина нашего массива меньше запрашиваемого номера
        num = num * 2
        a = [i for i in range(num)]
        a[1] = 0
        b = []

        for i in range(2, num):  # начинается решето
            if a[i] != 0:
                j = i * 2
                while j < num:
                    a[j] = 0
                    j = j + i

        for i in a:
            if i != 0:
                b += [i]
    return b[n - 1]


def p_num_v2(n):
    b = []
    i = 2
    while True:
        if len(b) == n:  # добавляем элементы пока не настигнем нужную длину
            break
        if i % 2 == 0:  # проверка на четность
            if i == 2:
                b += [i]
        else:
            p = 3
            while p * p <= i and i % p != 0:  # проверяем делитель, не превосходящий квадратного корня из числа
                p += 2
            if p * p > i:
                b += [i]
        i += 1
    return b[-1]


start_ = 1000
end_ = 5000
step_ = start_

for i in range(start_, end_ + 1, step_):
    print(f'p_num номер числа {i} - {timeit("p_num(i)", number=100, globals=globals())}')

print(run('p_num(500)'))

for i in range(start_, end_ + 1, step_):
    print(f'p_num_v2 номер числа {i} - {timeit("p_num_v2(i)", number=100, globals=globals())}')

print(run('p_num_v2(500)'))

# p_num номер числа 1000 - 0.7402744619999999
# p_num номер числа 2000 - 2.9328348460000004
# p_num номер числа 3000 - 4.267792336
# p_num номер числа 4000 - 5.572382039999999
# p_num номер числа 5000 - 7.116811640999998

# p_num_v2 номер числа 1000 - 0.8976752579999996
# p_num_v2 номер числа 2000 - 2.4415614399999974
# p_num_v2 номер числа 3000 - 4.444725260000002
# p_num_v2 номер числа 4000 - 6.718573189000004
# p_num_v2 номер числа 5000 - 9.335593504999999

# p_num
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         3    0.000    0.000    0.000    0.000 les4_task2.py:10(<listcomp>)
#         1    0.003    0.003    0.003    0.003 les4_task2.py:5(p_num)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# p_num_v2
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.004    0.004    0.004    0.004 les4_task2.py:27(p_num_v2)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      3571    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: «Решето Эратосфена» в данном случае отрабатывает быстрее
# т.к. в этом алгоритме нет столь сложных проверок и перебор осуществляется быстрее.
# функцию p_num можно ускорить если определить длину массива через пи функцию
# (так мы избежим многократную генерацию массива)
