import random
from enemy import Enemy

class boss(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = random.randint(10, 20)
    def attack(self)
        print("OUCH!")
        return super().random.randint(1, self.attack_power)