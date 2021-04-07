'''7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''


class ComplexNumber:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __add__(self, other):
        return f'{self.number1 + other.number1} + {self.number2 + other.number2} * i'

    def __mul__(self, other):
        return f'{self.number1 * other.number1 - (self.number2 * other.number2)} + {self.number2 * other.number1} * i'


num1 = ComplexNumber(2, 2)
num2 = ComplexNumber(3, 3)
print(num1 + num2)
print(num1 * num2)