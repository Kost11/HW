a = float(input("Ведіть перше число: "))
s = (input("Ведіть знак : = ділити, * = помножити, - = мінус, + = плюс: "))
b = float(input("Ведіть друге число: "))

if s == ":":
    print(a / b)
elif s == "*":
    print(a * b)
elif s == "-":
    print(a - b)
elif s == "+":
    print(a + b)
