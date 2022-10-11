# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988


from decimal import Decimal


def calculattion_number(number, d):
    num1 = Decimal(number)
    num1 = num1.quantize(Decimal(d))
    return num1


number = input('Enter a real number:  ')
d = input(' Enter the required accuracy d:  ')
print(calculattion_number(number, d))
