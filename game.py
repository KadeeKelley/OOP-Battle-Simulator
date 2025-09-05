import random
from goblin import Goblin
from hero import Hero

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero(input("What would you like to name your hero?"))

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "pink") for i in range(3)]

    # Keep track of how many goblins were defeatedl
    defeated_goblins = 0
    total_damage = 0
    rounds = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        total_damage += damage 
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                #implementing special ability
                switcheroo = hero.special_ability()
                if switcheroo == False:
                    print(f"{goblin.name}'s attack has failed! It takes {damage} damage!")
                    target_goblin.take_damage(damage)
                    if not target_goblin.is_alive():
                        defeated_goblins += 1
                        print(f"{target_goblin.name} has been defeated!")
                else:
                    hero.defense(rounds)
                    hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print("Total damage dealt: " + str(total_damage))
    print("Total rounds fought: " + str(rounds))
if __name__ == "__main__":
    main()
