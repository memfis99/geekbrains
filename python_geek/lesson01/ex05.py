firm_rev = int(input("Введите значение выручки >>> "))
firm_cost = int(input("Введите значение издержки >>> "))
firm_rent = 0

if firm_rev > firm_cost:
    firm_rent = firm_rev - firm_cost / firm_rev
    print(f"Фирма получила прибыль. Рентабильность выручки {firm_rent}")
    firm_emp = int(input("Введте кол-во сотрудников >>> "))
    emp_profit = firm_rev - firm_cost / firm_emp
    print(f"Прибыль фирмы в расчете на одного сотрудника. {emp_profit}")
else:
    print("Фирма работает в убыток")
