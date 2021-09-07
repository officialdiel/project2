import random

oddelovac = "-" * 47
def uvod():
    print("Hi there!")
    print(oddelovac)
    print("I've generated a random 4 digit number for you.\n"
          "Let's play a bulls and cows game.")
    print(oddelovac)
    print("Enter a number:")
    print(oddelovac)

def cisla() -> str:
    list_cislic_int = [0]
    while list_cislic_int[0] == 0:
        list_cislic_int = random.sample(list(range(10)), 4)
    list_cislic_str = [str(i) for i in list_cislic_int]
    hadane = ''.join(list_cislic_str)
    return hadane


hadanka = cisla()

uvod()

pocitadlo = 0
while True:
    bull = 0
    cow = 0
    zadane_cislo = input()
    if not zadane_cislo.isdigit():
        print('Zadej čísla')
    elif len(zadane_cislo) != 4:
        print('Zadej čtyřmístné číslo')
    elif zadane_cislo[0] == '0':
        print('zadej čísla co nezačínají nulou')
    elif len(zadane_cislo) != len(set(zadane_cislo)):
        print('Stejné číslice')
    else:
        pocitadlo += 1
        if zadane_cislo == hadanka:
            print(f"Correct, you've guessed the right number {pocitadlo}. pokus.")
            oddelovac
            break
        else:
            for index, cislice in enumerate(zadane_cislo):
                if cislice in hadanka:
                    if cislice == hadanka[index]:
                        bull += 1
                    else:
                        cow += 1
            if bull == 1 and cow == 1:
                print(f'{bull} bull, {cow} cow')
                oddelovac
            elif bull == 1 and cow != 1:
                print(f'{bull} bull, {cow} cows')
                oddelovac
            elif bull != 1 and cow == 1:
                print(f'{bull} bulls, {cow} cow')
                oddelovac
            else:
                print(f'{bull} bulls, {cow} cows')
                oddelovac