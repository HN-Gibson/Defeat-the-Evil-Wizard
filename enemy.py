# Base Character class
import random


class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, player):
        damage = random.randint(self.attack_power-5,self.attack_power+5)
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        return

# EvilWizard class (inherits from Character)
class EvilWizard(Enemy):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=15)  
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        if self.health <=195:
            self.health += 5 
        else:
            self.health = self.max_health 
        print(f"{self.name} regenerates health! Current health: {self.health}")