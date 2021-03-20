# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys

"""нужно запускать с параметрами"""


def salary(work_hour, amount_in_hour, bonus):
    try:
        return work_hour * amount_in_hour + bonus
    except TypeError:
        return


file, WorkHours, AmountInHors, BonusEmp, = sys.argv

try:
    print(salary(int(WorkHours), int(AmountInHors), int(BonusEmp)))
except ValueError:
    print(f'Invalid argument for calculation salary')
