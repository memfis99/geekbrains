'''3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)'''


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        my_dict = {'gross': wage, 'bonus': bonus}
        self._income = my_dict


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{sum(self._income.values())}')


alex = Position('alex', 'doe', 'man', 50, 50)
kate = Position('Kate', 'middle', 'eng', 60, 60)
chuck = Position('Chuck', 'Norris', 'fighter', 70, 70)

alex.get_full_name()
alex.get_total_income()

kate.get_full_name()
kate.get_total_income()

chuck.get_full_name()
chuck.get_total_income()

