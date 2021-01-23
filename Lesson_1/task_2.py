# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
print('Введите три разных числа.')

num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = float(input('Введите третье число: '))
maximum = num1
minimum = num1

if maximum < num2:
    maximum = num2
if maximum < num3:
    maximum = num3

if minimum > num2:
    minimum = num2
if minimum > num3:
    minimum = num3

result = (num1 + num2 + num3) - (minimum + maximum)

print(f'Число {result} является средним')
