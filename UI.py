# Function to create player character based on user input
import character
import enemy
import counter
import random

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Hunter") 
    print("4. Paladin")  
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return character.Warrior(name)
    elif class_choice == '2':
        return character.Mage(name)
    elif class_choice == '3':
        return character.Hunter(name)
    elif class_choice == '4':
        # Add Paladin class here
        return character.Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return character.Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):

    skeleton_counter = counter.Counter()

    while wizard.health > 0 and player.health > 0:
        action_available = True
        player.blocking = False
        player.evading = False 
        player.countering = False
        while action_available == True:
            print("""
                --- Your Turn ---
            1. Use Special Ability 1
            2. Use Special Ability 2
            3. Use Health Potion
            4. View Character Stats and Abilities
                """)
            
            choice = input("Choose an action: ")    
            if choice == '1':
                player.special_ability_1 (wizard)
                action_available = False
            elif choice == '2':
                player.special_ability_2 ()
                action_available = False
            elif choice == '3':
                player.health_potion ()
                action_available = False
            elif choice == '4':
                player.display_stats ()
            else:
                print("Invalid choice, try again.")
                continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health >= 100:
            wizard.regenerate()
            if player.blocking == True or player.evading == True or player.countering == True:
                print ("The Dark Wizard sees you prepared and chooses to wait for an opening!")   
            else: 
                wizard.attack(player)


        elif wizard.health < 100 and wizard.health > 0:
            wizard.regenerate()
            print("The Dark Wizard summons two Skeletal Warriors from the corpses surrounding them!")
            skeleton_counter.increment()
            skeleton_counter.increment()
            if player.blocking == True:
                skeleton_damage = random.randint(1,4) * (skeleton_counter.get_value() - 1)
                player.health-= skeleton_damage
                print(f"You block the first attack, but then take {skeleton_damage} damage from the other {skeleton_counter.get_value() - 1} Skeleton Warrior(s)")
                print("You know you must defeat The Dark Wizard to stop the skeletons!")
            elif player.evading == True:
                skeleton_damage = random.randint(1,4) * (skeleton_counter.get_value() - 1)
                player.health-= skeleton_damage
                print(f"You dodge the first attack, but then take {skeleton_damage} damage from the other {skeleton_counter.get_value() - 1} Skeleton Warrior(s)")
                print("You know you must defeat The Dark Wizard to stop the skeletons!")     
            else:
                skeleton_damage = random.randint(1,4) * skeleton_counter.get_value()
                player.health-= skeleton_damage
                print(f"You take {skeleton_damage} damage from {skeleton_counter.get_value()} Skeleton Warriors")
                print("You know you must defeat The Dark Wizard to stop the skeletons!")

            if player.countering == True:
                print ("The Dark Wizard sees you have not lost focus and decides to let the skeletons do their job!")
            else:
                wizard.attack(player)               


        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = enemy.EvilWizard("The Dark Wizard")
    
    # Start the battle
    battle(player, wizard)