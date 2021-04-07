'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''


class MyDate:

    @classmethod
    def date_int(cls, d_date_int):
        d_date_int = d_date.replace('-', ',').split(',')
        for i in d_date_int:
            i = int(i)
            print(i)

    @staticmethod
    def valid_m(d_date_valid):
        day_year = ''
        valid_mount = ''
        dict_m = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль',
                  8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
        d_date_valid = d_date_valid.replace('-', ',').split(',')
        for i in d_date_valid:
            if i.isdigit():
                day_year = day_year + i + ' '
            elif not i.isdigit():
                for x, y in dict_m.items():
                    if y == i:
                        valid_mount = x
        print(day_year[0:2], valid_mount, day_year[3:7])


d_date = '02-12-1989'
d_date2 = '02-Март-1989'
print(MyDate.date_int(d_date))
print(MyDate.valid_m(d_date2))
