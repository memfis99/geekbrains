my_list = [7, 5, 3, 3, 2]
user_number = int(input('Write number >>> '))
f_max = max(my_list)
f_min = min(my_list)
# print(f_max, type(f_max), user_number, type(user_number), f_min, type(f_min))
while 1 > 0:
    if f_max < user_number:
        my_list.insert(0, user_number)
        print(my_list)
    elif f_min > user_number:
        my_list.append(user_number)
        print(my_list)
    else:
        my_list.append(user_number)
        my_list.sort(reverse=True)
        print(my_list)
    my_list = [7, 5, 3, 3, 2]
    try:
        user_number = int(input('write number (for exit press Enter) >>> '))
    except ValueError:
        break









#for i in my_list:
#    if i > user_number:
