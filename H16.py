from datetime import datetime
now = datetime.now()
def time():
    print(f"{now.hour}:{now.minute}")
def write():
    with open("L16.2", "wt") as file:
        file.write(f"{now.hour}:{now.minute}")
while 1 :
    print("0 - Завершити програму\n1 - Показати час\n2 - Записати час у файл")
    result = input(">>: ")
    if result == "1":
        time()
    elif result == "2":
        write()
    elif result == "0":
        break