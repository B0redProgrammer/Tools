
while True:
    command = input('>')

    if command == 'add':
        name = input('Name:')
        value = input('Value:')
        file = open("/home/sat/Documents/Code/Python/personal_programs/lookup_tables/created_tables/MathSigns.txt", "a")
        file.write(name + '|' + value + '\n')
        file.close()
    elif command == 'search':
        value = input('Search:')
        file = open('/home/sat/Documents/Code/Python/personal_programs/lookup_tables/created_tables/MathSigns.txt', 'r')

        for line in file.readlines():
            line = line.split('|')
            if line[0] == value:
                print('You searched {}'.format(value))
                print("Here's what we found: {}".format(line[1]))
                file.close()
    elif command == 'list':
        file = open('/home/sat/Documents/Code/Python/personal_programs/lookup_tables/created_tables/MathSigns.txt', 'r')

        for i, line in enumerate(file.readlines()):
            line = line.split('|')
            print('{}.{}={}'.format(i, line[0], line[1]))

    elif command == 'quit':
        break
