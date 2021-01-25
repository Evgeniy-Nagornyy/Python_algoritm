# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


def func(n, row=1, sum_row=1):
    print(row, end=',  ')  # Вывед для проверки
    if n == 1:
        return sum_row
    else:
        return func(n - 1, row / -2, sum_row + row)


num = int(input('Введите количество элементов ряда: '))

print(f'\nСумма элементов ряда = {func(num)}')
