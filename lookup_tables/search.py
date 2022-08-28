import os

value = input('>')
path = '/home/sat/Documents/Code/Python/personal_programs/lookup_tables/created_tables'

for filename in os.listdir(path):
    if filename.split('.')[1] == 'txt':
        file = open(path + '/' + filename, 'r')

        for line in file.readlines():
            line = line.split('|')

            if value in line[0]:
                print('This is what we found in the {} lookup table under the key {}: {}'.format(filename.split('.')[0], line[0], line[1]))
        file.close()
