'''1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

user_data = input(f'Write you data >>>')
split_str = '\n'
user_str = user_data+split_str
with open(r'data.txt', 'w') as my_file:
    my_file.writelines(user_str)
check_date = ''
while True:
    user_data = input(f'Write you data >>>')
    split_str = '\n'
    user_str = user_data + split_str
    if user_data != check_date:
        with open(r'data.txt', 'a') as my_file_write:
            my_file_write.writelines(user_str)
    else:
        break

data_open = open(r'data.txt')
print(f'You write in file data.txt >>>\n{data_open.read()}')
data_open.close()
