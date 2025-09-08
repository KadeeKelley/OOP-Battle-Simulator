import random
from enemy import Enemy

class Mean(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = random.randint(20, 40)
    def attack(self):
        if self.health > 190:
            print("Meanie: mwahahaha!")
        elif self.health > 160:
            print("Meanie: be scared !!!")
        elif self.health > 120:
            print ("Meanie: ow...")
        elif self.health > 80:
            print("Meanie: You really think thats gonna stop me?")
        elif self.health > 50:
            print("Meanie: okay that kinda hurt")
        elif self.health > 20:
            print("Meanie: OWWWWWW")
        elif self.health > 0:
            print("Meanie: OUCHHHH!! WHY!!!")
        return random.randint(1, self.attack_power)