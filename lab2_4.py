import re

filename = input('Введите название файла: ')

try:
    with open(filename, 'r') as f:
        lines = f.readlines()
except IOError as err:
    print(err)
    lines = []

lines = list(map(lambda x: x.rstrip(), lines))

for i,line in enumerate(lines):
    result = re.findall(r'\w+\s\w+\s=\s\d+', line)
    for res in result:
        if res != []:
            print('Строка {0}: найдено \'{1}\''.format(i+1,res))
    

