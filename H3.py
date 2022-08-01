while True:
    a = float(input("Ведіть перше число: "))
    s = (input("Ведіть знак : = ділити, * = помножити, - = мінус, + = плюс: "))
    b = float(input("Ведіть друге число: "))

    try:
        if s == ":":
            print(a / b)
        elif s == "*":
            print(a * b)
        elif s == "-":
            print(a - b)
        elif s == "+":
            print(a + b)
    except ZeroDivisionError:
        print("На нуль ділити не можна!")
        print("Можете спробувати знову: ")