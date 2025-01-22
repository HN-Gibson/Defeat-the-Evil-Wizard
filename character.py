import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, special_abilities, initial_value = False):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.special_abilities=special_abilities
        self.evading = initial_value
        self.blocking = initial_value
        self.countering = initial_value

    def attack(self, target):
        damage = random.randint(self.attack_power-5,self.attack_power+5)
        target.health -= damage
        print(f"\n{self.name} attacks {target.name} for {damage} damage!\n")
        if target.health <= 0:
            return print(f"{target.name} has been defeated!")

    def display_stats(self):
        return print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Average Attack Power: {self.attack_power}\nSpecial Abilities:\n{self.special_abilities}")

    def health_potion(self):
        health_potion = 35
        if self.health + health_potion > self.max_health:
            self.health = self.max_health
            return print(f"You've been returned to max health: {self.health}!")
        else:
            self.health += health_potion
            return print(f"You gained 25 health! Current health: {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, special_abilities = "\n1: Power Attack\n2: Rage\n")  # Boost health and attack power
        self.rage = False
    def special_ability_1(self, target):
        self.attack_power += 10
        print (f"You swing with all your might at The Dark Wizard!")
        Character.attack(self, target)
        self.attack_power -= 10
        return
    def special_ability_2(self):
        if self.rage == False:
            self.attack_power += 10
            print(f"Your Average Attack Power rose to {self.attack_power}")
            return self.rage == True
        else:
            print("You're already raging! You use Power Attack instead!")
            self.special_ability_1()

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=35, special_abilities = "\n1: Lightning Bolt\n2: Counterspell\n")  # Boost attack power
    def special_ability_1(self, target):
        self.attack_power += 10
        print (f"A string of lighting erupts from your finger and strikes The Dark Wizard!")
        Character.attack(self, target)
        self.attack_power -= 10
        return        
    def special_ability_2(self):
        self.countering = True
        print ("You prepare to counter the next spell from the wizard!")
        return

# Hunter class (inherits from Character)
class Hunter(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20, special_abilities = "\n1: Double Shot\n2: Evade\n")
    def special_ability_1(self, target):
        print (f"You fire a quick shot at The Dark Wizard!")
        Character.attack(self, target)
        print (f"You fire a quick shot at The Dark Wizard!")
        Character.attack(self, target)
    def special_ability_2(self):
        self.evading = True
        print ("You prepare to dodge the next attack!")



# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, special_abilities = "\n1: Smite\n2: Shield\n")
    def special_ability_1(self,target):
        self.attack_power = self.attack_power * 2
        print(f"You let loose a holy attack with your blessed hammer against The Dark Wizard!")
        Character.attack(self, target)
        self.attack_power = self.attack_power / 2
    def special_ability_2(self):
        self.blocking = True
        print ("You prepare to block the next attack!")