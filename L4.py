import random
while True:
    number = random.randint(1,1000000)
    print('Вгадай число між 1 і 10')
    count = 0
    while True:
        спроба = input()
        i = int(спроба)
        if i == number:
            count = count+1 
            print('Правильно')

            break
        elif i < number:
            count = count+1
            print('Бери більше')

        elif i > number:
            count = count+1
            print('Бери менше')

    print('Знадобилося %s спроб' %count)
    print("Можете спробувати знову: ")