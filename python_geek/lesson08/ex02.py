'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class ZeroDivException(Exception):

    def __str__(self):
        return f'zero division'


class UserDiv:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def user_div(self):
        result: int
        if self.number2 == 0:
            raise ZeroDivException()
        result = self.number1 / self.number2
        return result


user_number = UserDiv(1, 0)
try:
    print(UserDiv.user_div(user_number))
except ZeroDivException as error:
    print(error)
