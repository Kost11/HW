import time

class Job(object):
    def __init__(self):
        print("Вы идете на работу")
        self.name = input("Назовыте ваше ымя ? ")
        
    @property
    def KPAH(self):
      print("""           __
 _________/  \___________________________
[________       ________________________/
         \     /                        |
          |\|/|                         |  
          |/|\|                         |
          |\|/|                         |
          |/|\|                         |
          |\|/|                         ¿
          |/|\|
          |\|/|
          |/|\|
          |\|/|
          |/|\|
        __/____\__
        |========|
        O  O  O  O
=========================================""")
      time.sleep(0.3)    
      print("""           __
 _________/  \___________________________
[________       ________________________/
         \     /                        |
          |\|/|                         |  
          |/|\|                         |
          |\|/|                         |
          |/|\|                         |
          |\|/|                         |
          |/|\|                         |
          |\|/|                         ¿
          |/|\|
          |\|/|
          |/|\|
        __/___\__
        |========|
        O  O  O  O
=========================================""")
      time.sleep(0.3)    
      print("""           __
 _________/  \___________________________
[________       ________________________/
         \     /                        |
          |\|/|                         |  
          |/|\|                         |
          |\|/|                         |
          |/|\|                         |
          |\|/|                         |
          |/|\|                         ¿
          |\|/|
          |/|\|
          |\|/|
          |/|\|
        __/___\__
        |========|
        O  O  O  O
=========================================""")
      time.sleep(0.3)    

    
    # функция кормления кошки. 
    # При каждом кормлении вес кошки увеличивается на 30 граммов.
    def eat(self):
        if self.hunger == 5:
            print("Кошка не голодная")
        else:
            self.hunger += 1
            self.__w += 30
            print("Мур!")

    # функиция для игры с кошкой. 
    # При каждой игре с кошкой она теряет 5 грамм веса.
    def play(self):
        self.talk()
        self.__w -= 5
        if self.hunger > 0:
            self.hunger -= 1
        else:
            self.hunger = 1

# Основная функция для управления всей программой из меню.    
def main():

  CTPONKA = (Job)
  choice = None
  while choice != "0":
      print \
      ("""
      Что будем делать?
          
      0 - Выйти
      1 - Поуправлять кранам
      2 - Прирнуть с 30 етажа
      3 - Обліть начальніка бітоном
      4 - Поесть
      5 - Поспать
      """)
            
      choice = input(">>: ")
      print()

        # exit
  if choice == "0":
    print(name,":Я увальняюсь. Пока")
            
      # послушать
  elif choice == "1":
    CTPONKA.KPAH()
                 
        # поиграть
  elif choice == "3":
    CTPONKA.play()
  elif choice == "4":
    print("Вес: ", CTPONKA.weight, " гр. ")
            
        # неправильный ввод
  else:
    print("\nНеправильный ввод!")  
main() # вызов функции            
input()