# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

from random import choice


def poly_sum(expression1: str, expression2: str):
    with open(expression1, "r", encoding="utf-8") as my_f_1:
        with open(expression2, "r", encoding="utf-8") as my_f_2:
            first = my_f_1.readlines()
            second = my_f_2.readlines()

            if len(first) == len(second):
                with open('expression_sum.txt', "a", encoding="utf-8") as my_f_3:
                    for i, v in enumerate(first):
                        my_f_3.write(f"{v[:-5]} + {second[i]}")
            else:
                print("The contents of the files do not match!")


expression1 = 'C:\\Users\\vasil\\Documents\\репозитории\\python_4_seminar_dz\\expression1 .txt'
expression2 = 'C:\\Users\\vasil\\Documents\\репозитории\\python_4_seminar_dz\\expression2 .txt'

result = poly_sum(expression1, expression2)
poly_sum(result)
