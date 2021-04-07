'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.'''


class TechnicStorage:
    technic_type: str
    technic_prize: int
    technic_model: str
    technic_count: int

    def __init__(self, technic_type, technic_prize, technic_model, technic_count, ):
        self.technic_type = technic_type
        self.technic_prize = technic_prize
        self.technic_model = technic_model
        self.technic_count = technic_count
        self.my_store = []
        self.my_dict = {'Тип техники': self.technic_type, 'цена за единицу': self.technic_prize,
                        'Колличесство': self.technic_count}

    def __str__(self):
        return f'Тип техники {self.technic_type}, цена за единицу {self.technic_prize},' \
               f'Колличесство {self.technic_count}'

    def add_to_storage(self):
        tech_type = input(f'Введите тип техники')
        tech_prize = int(input(f'Укажите цену'))
        tech_count = input(f'Укажите колличество')
        tech_dict = {'Тип техники': tech_type, 'цена за единицу': tech_prize, 'Колличесство': tech_count}
        self.my_dict.update(tech_dict)
        self.my_store.append(tech_dict)
        print(f'Текущий список -\n {self.my_store}')


class Printer(TechnicStorage):
    def print(self):
        return f'to print  {self.technic_count} '


class Scanner(TechnicStorage):
    scanner_model: str

    def scanner(self):
        return f'to scanner  {self.technic_count} '


class Xerox(TechnicStorage):
    xerox_model: str

    def xerox(self):
        return f'to xerox  {self.technic_count} '


unit1 = Printer('hp', 1000, 'print1', 5)
unit2 = Scanner('Canon', 2000, 'Scan1', 10)
unit3 = Xerox('Xerox', 3000, 'Copier1', 15)
print(unit1.add_to_storage())
print(unit2.add_to_storage())
print(unit3.add_to_storage())
print(unit1.print())
print(unit3.xerox())
