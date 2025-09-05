import random
from enemy import Enemy

class baby_elf(Enemy):
    def take_damage(self,damage):
        print("Why are you hitting the baby elf! YOU MONSTER !!!")
        return super().take_damage(damage)

