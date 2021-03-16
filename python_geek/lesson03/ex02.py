# 2. Реализовать функцию,
# принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

first_name = input('Write you name >>> ')
last_name = input('Write you last name >>> ')
user_year = input('Write you year of birth >>> ')
user_city = input('Write you city >>> ')
user_email = input('Write you email >>> ')
user_phone = input('Write you phone >>> ')


def user_data(f_first_name=first_name, f_last_name=last_name, f_user_year=user_year, f_user_city=user_city,
              f_user_email=user_email, f_user_phone=user_phone):
    print(f'user data {f_first_name,f_last_name,f_user_year,f_user_city,f_user_email,f_user_phone}')


user_data()
