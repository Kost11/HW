import random
import time

class Cat(object):
    """ Виртуальная кошка """
    fatigue = 100    
    total = 0 # сколько кошек изначально
    # Декоратор в Python – это функция, которая принимает другую функцию 
    # в качестве аргумента. 

    # Декоратор начинается с символа @, за которым следует название функции, 
    # которую мы собираемся «декорировать»

    # Декоратор @staticmethod — это просто функция внутри класса. 
    # Вы можете вызывать их обоих как с инициализацией класса 
    # так и без создания экземпляра класса. 

    # Обычно это применяется в тех случаях, когда у вас есть функция, 
    # которая, по вашему убеждению, имеет связь с классом. 

    # Проще говоря, @staticmethod — это вроде обычной функции, 
    # определенной внутри класса, которая не имеет доступа к экземпляру, 
    # поэтому ее можно вызывать без создания экземпляра класса.

    @staticmethod
    # функция для счета количества кошек
    def count():
        print("Всего кошек: ", Cat.total)
    
    #  метод __init__ принимает аргументы для нашего класса
    def __init__(self):
        print("Родилась новая кошка!")
        self.name = input("Как мы её назовём? ") # даем имя кошки при рождении
        Cat.total += 1 # счетчик кошек (при рождении +1)
        self.__w = 300 # начальный вес кошки __w это закрытый атрибут
        self.hunger = 1# начальный голод кошки
        self.fatigue = 100
        
    # метод __str__ отвечает за строкое представление объекта
    def __str__(self):
        res = "Объект класса Cat\n name: " + self.name + "\nBec: " + str(self.__w) 
        # метод str() возвращает строку
        return res # Оператор return используется в функциях 
        #для возвращения данных после выполнения работы самой функции.

    # @property в Python – один из встроенных декораторов. 

    # Основная цель любого декоратора – изменить методы или атрибуты 
    # вашего класса таким образом, 
    # чтобы пользователю вашего класса не нужно было 
    # вносить какие-либо изменения в свой код.

    @property
    # функция веса кошки. Берет из закрытого атрибута
    def weight(self):
        return self.__w
    
    # функция рождения кошки и его первого мяу..
    def talk(self):
        print(self.name, ": Мяу")
    
    # функция кормления кошки. 
    # При каждом кормлении вес кошки увеличивается на 30 граммов.
    def eat(self):
        if self.hunger == 3:
            print("Кошка не хочет есть")
        else:
            self.hunger += 1
            self.__w += 30
            print("Хрум-хрум-хрум")

    # функиция для игры с кошкой. 
    # При каждой игре с кошкой она теряет 5 грамм веса.
    def play(self):
        a = random.randint(1,3)
        if a == 1:
            print("Кошка не хочет играть")
        else:
            self.talk()
            self.__w -= 5
            if self.fatigue > 0:
                self.fatigue -= 20
            else:
                self.fatigue = 0

            if self.hunger > 0:
                self.hunger -= 1
            else:
                self.hunger = 1

    def sleep(self):
        if self.fatigue == 100:
            print("Кошка не хочет спать")
        else:
            if self.fatigue < 100 and self.fatigue > 80:
                time.sleep(180)
                self.fatigue = 100
                print("Кошка поспала")
            elif self.fatigue < 80 and self.fatigue > 60:
                time.sleep(180 * 2)
                self.fatigue = 100
                print("Кошка поспала")
            elif self.fatigue < 60 and self.fatigue > 40:
                time.sleep(180 * 3)
                self.fatigue = 100
                print("Кошка поспала")
            elif self.fatigue < 40 and self.fatigue > 20:
                time.sleep(180 * 4)
                self.fatigue = 100
                print("Кошка поспала")
            elif self.fatigue < 20 and self.fatigue > 0:
                time.sleep(180 * 5)
                self.fatigue = 100
                print("Кошка поспала")

# Основная функция для управления всей программой из меню.    
def main():

    bagira = Cat()
    choice = None
    while choice != "0":
        print \
        ("""
        Что будем делать?
            
        0 - Выйти
        1 - Поговорить с кошкой
        2 - Покормить
        3 - Поиграть
        4 - Взвесить
        5 - Оставить спать
        """)
            
        choice = input(">>> ")
        print()

        if self.fatigue == 0:
            print("кошка очень усталаей нужно поспать")

        # exit
        elif choice == "0":
            print("Пока.")
            
        # послушать
        elif choice == "1":
            bagira.talk()
                
        # покормить
        elif choice == "2":
            bagira.eat()
                
        # поиграть
        elif choice == "3":
            bagira.play()
        
        elif choice == "4":
            print("Вес: ", bagira.weight, " гр. ")
        
        elif choice == "5":
            bagira.sleep

        # неправильный ввод
        else:
            print("\nНеправильный ввод!")  

        if fatigue <= 0:
            print("Кошка хочет спать")

        print(fatigue)

main() # вызов функции            
input()