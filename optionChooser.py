from random import randint

numOptions = int(input("How mant options do you have: "))

options = []

for i in range(numOptions):
    options.append(input("Option: "))


def randChoice(list):
    loops = randint(1, randint(1, 100))

    for i in range(loops):
        choice = randint(0, len(list) - 1)

    print("Do " + list[choice])

    if (input("Go Again: ") == "Y"):
        return randChoice(list)


randChoice(options)
