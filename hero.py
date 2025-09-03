import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defense: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.attack_power = random.randint(40, 50)
    

    def strike(self):
       critical = random.randint(1,30)
       if critical == 30:
           return (random.randint(15, self.attack_power)*2)
       if critical == 1:
           self.health -=3
           return 0
       return random.randint(15, self.attack_power)
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            new_health = "0"
        else:
            new_health = self.health
        print(f"{self.name} takes {damage} damage. Health is now {new_health}.")
    
    def is_alive(self):
        return self.health > 0
    
    def defense(self, rnd):
        if int(rnd) < 10:
            self.health += 10-(int(rnd))
            print("hero isn't tired yet! they regain " + str(10-(int(rnd))) + " health!")
        
    def special_ability(self):
        switch = random.randint(1,20)
        switcheroo = True
        if switch ==  20:
            switcheroo = False
        return switcheroo



