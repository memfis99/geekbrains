# 5. Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ,
# выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

count = 0

while True:
    user_num = user_num_check = input('write number(separator space) >>>')
    num_int = []
    user_num_check = user_num_check.replace(' ', '').isdigit()
    user_num = user_num.replace(' ', ' ,').replace(',', '').split()
    for i in user_num:
        if i.isdigit():
            num_int.append(int(i))
    count += sum(num_int)
    print(f' You sum result >>> {count}')
    if not user_num_check:
        print('Exit you write not digit, please try again')
        break


