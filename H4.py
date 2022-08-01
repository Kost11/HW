import random
a = int(input("Скільки символів ви хочете в паролі "))
def random_letter():
    letter = random.randint(1,26)
    if letter == 1:
        print("a")
    elif letter == 2:
        print("b")
    elif letter == 3:
        print("c")
    elif letter == 4:
            print("d")
    elif letter == 5:
        print("e")
    elif letter == 6:
        print("f")
    elif letter == 7:
        print("g")
    elif letter == 8:
        print("h")
    elif letter == 9:
        print("i")
    elif letter == 10:
        print("j")
    elif letter == 11:
        print("k")
    elif letter == 12:
        print("l")
    elif letter == 13:
        print("m")
    elif letter == 14:
        print("n")
    elif letter == 15:
        print("o")
    elif letter == 16:
        print("p")
    elif letter == 17:
        print("q")
    elif letter == 18:
        print("r")
    elif letter == 19:
        print("s")
    elif letter == 20:
        print("t")
    elif letter == 21:
        print("u")
    elif letter == 22:
        print("v")
    elif letter == 23:
        print("w")
    elif letter == 24:
        print("x")
    elif letter == 25:
        print("y")
    elif letter == 26:
        print("z")

def random_number():
    number = random.randint(0,9)
    print(number)

#a = random.randint(2,6)

for c in range(a):
    d = random.randint(1,2)
    if d == 1:
        random_letter()
    else:
        random_number()