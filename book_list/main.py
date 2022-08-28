import random

while True:
    action = input(">")

    if action == "add":
        file = open("/home/sat/Documents/Code/Python/personal_programs/book_list/list.txt", "a")

        added_book = input("Book name:")
        genre = input("genre:")

        file.write(added_book + "|" + genre + "\n")

    elif action == "remove":
        file = open("/home/sat/Documents/Code/Python/personal_programs/book_list/list.txt", "r")
        book = input("Name:")
        lines = file.readlines()
        file.close()

        file = open("/home/sat/Documents/Code/Python/personal_programs/book_list/list.txt", "w")
        for line in lines:
            if book not in line:
                file.write(line)
        file.close()

    elif action == "random":
        afile = open("/home/sat/Documents/Code/Python/personal_programs/book_list/list.txt", "r")
        line = next(afile)
        for num, aline in enumerate(afile, 2):
            if random.randrange(num):
                continue
            line = aline.split("|")
        print("{}, Genre: {}".format(line[0], line[1]))

    elif action == "genre":
        file = open("/home/sat/Documents/Code/Python/personal_programs/book_list/list.txt", "r")
        genre = input("Genre: ")

        for line in file.readlines():
            line = line.split("|")
            if genre in line[1]:
                print(line[0])

    elif action == "list":
        file = open("/home/sat/Documents/Code/Python/personal_programs/book_list/list.txt", "r")

        for i, line in enumerate(file):
            line = line.split("|")
            print("{}.{}, Genre: {}".format(i+1, line[0], line[1]))

    elif action == "quit":
        break
