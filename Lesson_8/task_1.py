# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку


def substrings(string):
    result = []
    for i in range(len(string) + 1):
        for j in range(len(string) + 1):
            if hash(string[i:j]) not in result:  # функции hash достаточно (не требуется постоянная работа)
                result += [hash(string[i:j])]
    return len(result) - 2  # убираем варианты пустой строки и полной строки


print(substrings('papa'))
