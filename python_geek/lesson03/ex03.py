# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

arg1 = int(input('Write arg 1 in int >>> '))
arg2 = int(input('Write arg 2 in int >>> '))
agr3 = int(input('Write arg 3 in int >>> '))


def max_sum(a1=arg1, a2=arg2, a3=agr3):
    all_arg = [a1, a2, a3]
    max_arg1 = max(all_arg)
    all_arg.remove(max_arg1)
    max_arg2 = max(all_arg)
    return max_arg1 + max_arg2


print(f'Sum 2 max arg  is {max_sum()}')
