import random
import pathlib

while True:
    action = input(">")

    path = pathlib.Path(__file__).parent.resolve()

    if action == "add":
        file = open("{}/list.txt".format(path), "a")

        added_book = input("Book name:")
        genre = input("genre:")

        file.write(added_book + "|" + genre + "\n")

    elif action == "remove":
        file = open("{}/list.txt".format(path), "r")
        book = input("Name:")
        lines = file.readlines()
        file.close()

        file = open("{}/list.txt".format(path), "w")
        for line in lines:
            if book not in line:
                file.write(line)
        file.close()

    elif action == "random":
        afile = open("{}/list.txt".format(path), "r")
        line = next(afile)
        for num, aline in enumerate(afile, 2):
            if random.randrange(num):
                continue
            line = aline.split("|")
        print("{}, Genre: {}".format(line[0], line[1]))

    elif action == "genre":
        file = open("{}/list.txt".format(path), "r")
        genre = input("Genre: ")

        for line in file.readlines():
            line = line.split("|")
            if genre in line[1]:
                print(line[0])

    elif action == "list":
        file = open("{}/list.txt".format(path), "r")

        for i, line in enumerate(file):
            line = line.split("|")
            print("{}.{}, Genre: {}".format(i+1, line[0], line[1]))

    elif action == "quit":
        break
