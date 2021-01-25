#https://drive.google.com/file/d/1U6PAid3r5YFm3V_0_hN62n_gQ9xHyF14/view?usp=sharing

# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.


def calc(a, operation, b):
    if operation == '+':
        return f'{a + b = }'
    elif operation == '-':
        return f'{a - b = }'
    elif operation == '*':
        return f'{a * b = }'
    elif operation == '/':
        if b != 0:
            return f'{a / b = :.1f}'
        else:
            return 'Ошибка: деление на 0'


while True:
    oper = str(input('Для завершения введите 0\nВведите действие +, -, *, / : '))
    if oper in '0+-*/':  # проверяем, есть ли у нас действие, которое ввел пользователь
        if oper == '0':  # проверяем, хочет ли пользователь выйти из программы
            print('Операция завершена')
            break
        else:
            num_1 = float(input('Введите первое число: '))
            num_2 = float(input('Введите второе число: '))
            print(calc(num_1, oper, num_2))
    else:
        print('Ошибка: такого действия не существует')
