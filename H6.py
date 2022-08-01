def a():
    a = int(input("Скільки кілометрів? ")) * 1000 / 140
    b = 400
    b = b + 25 * a
    b = b // 1 / 100
    print(b,"$")

while True:
    a()
    print("Можете спробувати знову: ")