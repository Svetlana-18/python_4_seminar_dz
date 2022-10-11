# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in 54    out  [2, 3, 3, 3]       in 9990    out [2, 3, 3, 3, 5, 37]     in 650  out [2, 5, 5, 13]


def create_list_multipliers(num):
    create_list = []
    d = 2
    while num > 1:
        if num % d == 0:
            create_list.append(d)
            num //= d
        else:
            d += 1
    return create_list


number = (int(input('Задайте натуральное число N: ')))
if number <= 0:
    print('Ошибка ввода, введите натуральное положительное число')
else:
    print(create_list_multipliers(number))
