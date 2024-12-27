import random

class Animal:                             # животные
    _DEGREE_OF_DANGER = 0                 # степень опасности
    live = True
    sound = None                          # звук отсутствует

    def __init__(self,  speed):
        self._cords = [0, 0, 0]             # координаты
        self.speed = speed                # скорость передвижения

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
             print(f"Sorry, i'm peaceful :)")

        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):                         # птицы
    beak = True                             # наличие клюва

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):                # плавующие животные
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - int(abs(dz) * (self.speed /2 ))  # скорость при нырянии

class PoisonousAnimal(Animal):                   # ядовитые животные
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):  #  утконос
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"               # звук утконоса

    def speak(self):
        print (self.sound)

db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
