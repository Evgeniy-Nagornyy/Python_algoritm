
# https://drive.google.com/file/d/1dGToNeTugOz1i7WFbPWIwNXrODjBHeAh/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input('Введите целое трехзначное число: '))

num1 = n // 100
num2 = (n // 10) - (n // 100) * 10
num3 = n - ((n // 10) * 10)
s = num1 + num2 + num3
p = num1 * num2 * num3

print(f'Сумма чисел составляющих число n = {s}')
print(f'Произведение чисел составляющих число n = {p} ')

'''
Можно было конечно решить и так:

n = int(input('Введите целое трехзначное число: '))
print(f'Сумма чисел составляющих число n = {(n//100) + ((n//10) - (n//100)*10) + (n-((n//10)*10))}\n '
      f'Произведение чисел составляющих число n = {(n//100) * ((n//10) - (n//100)*10) * (n-((n//10)*10))}')
      
Но в чем тогда смысл)))))
'''
