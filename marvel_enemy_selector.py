"""
AUTHOR: Faith Moselle O. Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023

PROGRAM: Marvel Universe Enemy Selector
LANGUAGE: Python 3
TOPIC: Object-Oriented Programming (OOP) - Classes and Objects
TECH STACK: Python Standard Library

DESCRIPTION:
An enemy selection program set in the Marvel Universe. Iron Man (user) chooses an opponent from three Avengers: Captain America, Thor, or Black Widow.
The program displays each enemy's level, special skill, and damage capability.

CLASS STRUCTURE:
- Enemy class: Blueprint for creating enemy/hero objects
- Attributes: hero (name), level (power level), skill (special ability), damage (attack power)
- Methods: display() - returns formatted enemy information

GAME CONTEXT:
- Player assumes role of Iron Man
- Must choose an enemy to fight
- Each enemy has unique stats and abilities
"""

# ============================================================================
# CLASS DEFINITION - Blueprint for Enemy/Hero objects
# ============================================================================

class Enemy:
    """
    Enemy class representing a combat opponent in the Marvel Universe.
    
    Attributes:
        hero (str): Name of the enemy hero/villain
        level (str/int): Power level of the enemy
        skill (str): Special ability or combat skill
        damage (str): Damage output capability
    """
    
    def __init__(self, hero, level, skill, dam):
        """
        Constructor method - Initializes a new Enemy object.
        
        Called automatically when creating a new Enemy instance.
        
        Args:
            hero (str): Name of the enemy (e.g., "Captain America")
            level (str/int): Power level of the enemy
            skill (str): Special skill or ability
            dam (str): Damage percentage or description
        """
        self.hero = hero      # Enemy name identifier
        self.level = level    # Power level rating
        self.skill = skill    # Special combat ability
        self.damage = dam     # Attack damage capability

    def display(self):
        """
        Returns formatted string containing all enemy information.
        
        Uses escape sequences:
        - \n : New line
        - \t : Tab indent
        
        Returns:
            str: Formatted text with enemy details (name, level, skill, damage)
        """
        return f"Your enemy: {self.hero}\n\tLevel: {self.level}\n\tSkill: {self.skill}\n\tDamage: {self.damage}"


# ============================================================================
# CREATE ENEMY OBJECTS (Instances of the Enemy class)
# ============================================================================

# Create 3 different enemy objects representing Avengers heroes
hero1 = Enemy("Captain America", "5", "Shield", "80% Damage")
hero2 = Enemy("Thor", "80", "Lightning Hammer", "80% Damage")
hero3 = Enemy("Black Widow", "100", "Trained Assassin", "100% Damage")

# ============================================================================
# MAIN PROGRAM LOOP - USER INTERFACE FOR ENEMY SELECTION
# ============================================================================

while True:
    # Display menu and get user input (player assumes role of Iron Man)
    enemy = int(input("Marvel Universe\n Welcome Iron Man, kindly choose your enemy!\n\tEnemy 1: Captain America\n\tEnemy "
                      "2: Thor\n\tEnemy 3: Black Widow\n\nYour chosen enemy number: "))
    
    # Selection logic - display corresponding enemy information
    if enemy == 1:
        print(hero1.display())  # Show Captain America stats
        break                    # Exit loop after valid selection
    elif enemy == 2:
        print(hero2.display())  # Show Thor stats
        break
    elif enemy == 3:
        print(hero3.display())  # Show Black Widow stats
        break
    else:
        # Invalid input handling - prompts user again
        print("Please enter the number of your chosen enemy 1-3:")

# Program ends - user has selected their enemy and seen their stats
