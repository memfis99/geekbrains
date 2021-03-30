'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т'''


class Road:
    _length_r = 5000
    _width_r = 20
    weight: int
    thick: int

    def __init__(self, weight, thick, _length_r=5000, _width_r=20):
        self.weight = weight
        self.thick = thick
        self._length_r = _length_r
        self._width_r = _width_r

    def calc_sum(self):
        total_sum = self._length_r * self._width_r * self.weight * self.thick/1000
        print(round(total_sum))


sum_calc = Road(25, 5)

sum_calc.calc_sum()
