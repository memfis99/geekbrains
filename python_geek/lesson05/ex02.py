'''2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.'''

with open('data_file_ex02.txt.') as f:
    lines = f.readlines()


with open('our_output.txt', 'w') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        f.write('Line number {} has {} words.\n'.format(index + 1, number_of_words))


