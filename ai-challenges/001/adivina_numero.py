import random


def validador(texto):
    while True:
        try:
            numMAX = int(input(texto))
            break
        except:
            print("error")
    return numMAX


numMAX= validador("elige max: ")
numU = None
numR = random.randint(0, numMAX)


while numU != numR:
    numU = validador("adivina el numero: ")
    if numU == numR:
        print("YOU WINNNN")
    elif numU < numR:
        print("the number is greater")
    elif numU > numR:
        print("the number is less")