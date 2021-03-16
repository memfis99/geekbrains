# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

user_num1 = int(input(f'Write number1 >>>'))
user_num2 = int(input(f'Write number2 >>>'))


def numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"division by zero >>> please try again")


user_num_total = numbers(user_num1, user_num2)
print(user_num_total)
