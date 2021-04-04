'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, clothes_diff: int):
        self.clothes_diff = clothes_diff

    @abstractmethod
    def calc_sum(self):
        pass


class Coat(Clothes):
    def calc_sum(self):
        cost_coat = self.clothes_diff / 6.5 + 0.5
        return f'need for Coat {cost_coat}'


class Suit(Clothes):
    def calc_sum(self):
        cost_suit = 2 * self.clothes_diff + 0.3
        return f'need for suit {cost_suit}'


coat_inst = Coat(50)
suit_inst = Suit(100)

#coat_inst2 = Clothes(50)
#suit_inst2 = Clothes(100)

print(suit_inst.calc_sum())
print(coat_inst.calc_sum())
#print(coat_inst2.calc_sum)
