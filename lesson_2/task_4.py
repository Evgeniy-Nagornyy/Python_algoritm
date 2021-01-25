# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def func(num, line=''):
    if num == 0:
        return f'{line}'
    else:
        line += str(num % 10)
        return func(num // 10, line)


number = int(input('Введите натуральное число: '))
print(func(number))
