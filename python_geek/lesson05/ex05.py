'''5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

numbers = '12 22 34 45 56 67 780'
count = 0
with open(r'file_ex05.txt', 'w') as my_file:
    my_file.writelines(numbers)

with open(r'file_ex05.txt', 'r') as my_file_read:
    my_list = my_file_read.read().split(' ')
    for i in my_list:
        count += int(i)

print(count)


