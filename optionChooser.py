from random import randint

options = []
tmpOption = ""

while True:
    tmpOption = input("Option: ")

    if (tmpOption == ""):
        break

    options.append(tmpOption)


def randChoice(list):
    loops = randint(1, randint(1, 100))

    for _ in range(loops):
        choice = randint(0, len(list) - 1)

    print("Do " + list[choice])

    if (input("Go Again: ") == "Y"):
        return randChoice(list)


randChoice(options)
