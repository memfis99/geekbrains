check_int = 5
check_float = 5.5
check_list = [6, 7, 8, 9]
check_dict = {10, 11, 12, 13}
check_tuple = (14, 15, 16)
check_str = 'is string'

check_all = [check_int, check_float, check_list, check_dict, check_tuple, check_str]

for i in check_all:
    print(f"{i} is {type(i)}")
