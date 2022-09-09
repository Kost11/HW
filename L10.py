import random

class TBAPIHI:
    def __init__(self):
        pass

    def EAT (self, a):
        if a == 1:
            print("тварина їсть зелень")
        else:
            print("тварина їсть м'ясо")
    
    def sleep (self, b):
        if b == 1:
            print("тварина спить у день")
        else:
            print("тварина спить у ночі")

c = TBAPIHI()
d = TBAPIHI()
e = random.randint(1, 2)
f = random.randint(1, 2)

c.sleep(e)
d.EAT(f)