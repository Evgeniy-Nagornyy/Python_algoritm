# Посчитать четные и нечетные цифры введенного натурального числа.Например, если введено число 34560,
# в нем 3 четные цифры(4, 6 и 0) и 2 нечетные(3 и 5).


def func(num, even=0, odd=0):
    if num == 0:
        return f'{even = } {odd = }'
    else:
        if ((num % 10) % 2) == 0:
            return func(num // 10, even + 1, odd)
        else:
            return func(num // 10, even, odd + 1)


number = int(input('Введите натуральное число: '))
print(func(number))
