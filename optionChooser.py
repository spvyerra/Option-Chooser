from random import randint

numOptions = int(input("How mant options do you have: "))

options = []

for i in range(numOptions):
    options.append(input("Option: "))


while True:
    choice = randint(0, len(options) - 1)    
    
    print("Do " + options[choice])

    again = input("Go again? ")
    
    if (again == "Y"):
        continue

    break
