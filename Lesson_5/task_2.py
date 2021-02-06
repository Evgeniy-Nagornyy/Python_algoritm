# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

num10_dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
num16_dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
             10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


#  функция перевода в привычный для нас вид
def t_form(num):
    result = []
    for i in num:
        result += [num10_dic[i]]
    return result


# функция сложения
def sum_16(a, b):
    a = t_form(a)
    b = t_form(b)
    if len(a) < len(b):
        a, b = b, a
    result = deque(a)
    for i in range(1, len(b) + 1):
        result[-i] = result[-i] + b[-i]
    ost = 0
    for i in range(1, len(result) + 1):
        result[-i] += ost
        ost = result[-i] // 16
        result[-i] = (result[-i] % 16)
    result_end = ''.join([num16_dic[i] for i in result])
    return result_end


print('Сложение двух шестнадцатеричных чисел.')
num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
print(f'Сумма чисел {num1} и {num2} = {sum_16(num1, num2)}')
