# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите год: '))

if year / 4 == year // 4:
    if year / 100 == year // 100:
        if year / 400 == year // 400:
            print(f'{year} год високосный (366 дней)')
        else:
            print(f'{year} год не високосный (365 дней)')
    else:
        print(f'{year} год високосный (366 дней)')
else:
    print(f'{year} год не високосный (365 дней)')
