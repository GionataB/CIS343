################################################################################
# The Characters module defines classes about the types of game characters.
# There are two main type of characters, non-playable characters (NPCs) and
# playable characters (PCs). Since this game is to be played alone, the only PC
# is the player.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################

import random
import observe
import items

################################################################################
# A NPC is a a type of character that cannot be "controlled" by the user.
# NPCs usually are enemies (they want to "kill" the player), with one exception:
# other people that are not the player.
# A NPC inherit from the Observable object.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class NPC(observe.Observable):

    ############################################################################
    # The constructor defines the instance variables for a NPC object.
    # A NPC has a name, an health value, a minimum damage that can inflict, a
    # maximum damage that can inflict, a boolean value that describe the NPC as
    # damageable by the player, or not, and a list of weaknesses and/or
    # immunities.
    # @param self a pointer to the current object.
    # @param name the name of the NPC.
    # @param health the health value of the NPC.
    # @param minDamage the minimum damage the NPC can inflict.
    # @param maxDamage the maximum damage the NPC can inflict.
    # @param canBeDamaged if it is false, the NPC will be invincible.
    # @param modifier a dictionary of weaknesses and/or immunities.
    ############################################################################
    def __init__(self, name, health, minDamage, maxDamage, canBeDamaged, modifier):
        observe.Observable.__init__(self)
        self.name = name #The type of NPC
        self.health = health #The NPC's health
        self.minDamage = minDamage #The NPC's minimum damage it can deal
        self.maxDamage = maxDamage #The NPC's maximum damage it can deal
        self.can_be_damaged = canBeDamaged #Tells if the NPC is invincible or not
        self.modifier = modifier #A dictionary of weaknesses and immunities. They are both considered damage modifiers.

    ############################################################################
    # Get method to access the can_be_damaged field value.
    # @param self a pointer to the current object.
    # @return if the NPC can be damaged or not.
    ############################################################################
    def canBeDamaged(self):
        return self.can_be_damaged

    ############################################################################
    # Get method to access the name field value.
    # @param self a pointer to the current object.
    # @return the NPC's name.
    ############################################################################
    def getName(self):
        return self.name

    ############################################################################
    # Randomly choose an attack value the NPC will inflict, chosen between
    # the minimum and maximum damage.
    # @param self a pointer to the current object.
    # @return a randomly chosen attack value.
    ############################################################################
    def attack(self):
        return random.randint(self.minDamage, self.maxDamage)

    ############################################################################
    # Decrease the NPC's health by the damage value. If the NPC can't be damaged,
    # the health won't decrease.
    # If the health reaches zero, the NPC will let the house they are in know to
    # replace it with a Person.
    # @param self a pointer to the current object.
    # @param damage the amount of health lost.
    ############################################################################
    def damage(self, damage):
        if(self.can_be_damaged): #Decrease the NPC's health only if it can be damaged.
            self.health -= damage #Inflict the damage
            if(self.health <= 0):
                for observer in self.observers:
                    observer.update(self) #Change the monster back to a person

    ############################################################################
    # Given a weapon type, the function checks the dictionary and retrieves the
    # modifier for that weapon on the NPC. If the value is not in the dictionary,
    # the NPC is neither weak nor immune to the weapon, so a standard 1.0 will
    # be returned.
    # @param self a pointer to the current object.
    # @return a modifier for the damage on the NPC.
    ############################################################################
    def getModifier(self, weaponName):
        if(weaponName in self.modifier): #Check that the weapon is in the dictionary
            return self.modifier[weaponName]
        return 1.0 #The npc does not have a modifier for that weapon

################################################################################
# A Player is the user's avatar in the game. It is different from a NPC because
# it has a strength value (instead of a flat attack value), and an inventory of
# weapons. The strength itself is not a measure of the damage a Player can
# inflict, but it will be modified by the weapon used and on what NPC is used.
# The Player inherits from the Observable class, and is observed by the Game.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class Player(observe.Observable):

    ############################################################################
    # The constructor defines a Person object, with its field variables.
    # The health is randomly chosen between 100 and 125, while the strength is chosen
    # between 10 and 20.
    # The inventory keeps 10 weapons, one is always an HersheyKiss, a type of
    # non-consumable weapon, while the other 9 are randomly chosen.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        observe.Observable.__init__(self)
        self.health = random.randint(100, 125) #The health value. The player loses when the health reaches 0 (or less)
        self.strength = random.randint(10, 20) #The raw strength. the damage inflicted is calculated using the raw strength multiplied by some modifiers
        self.inventory = [items.HersheyKiss()] #The inventory has to have at least one HersheyKiss
        weapon = 0 #Make sure that there is no error in the first random weapon
        for i in range(9): #Randomly choose the other 9 weapons
            weapon = random.randint(1, 4)
            if(weapon == 1):
                self.inventory.append(items.HersheyKiss())
            elif(weapon == 2):
                self.inventory.append(items.SourStraw())
            elif(weapon == 3):
                self.inventory.append(items.ChocolateBar())
            elif(weapon == 4):
                self.inventory.append(items.NerdBomb())

    ############################################################################
    # Get method to access the health field value.
    # @param self a pointer to the current object.
    # @return the Player's health.
    ############################################################################
    def getHealth(self):
        return self.health

    ############################################################################
    # Calculate the damage on a NPC. The damage formula is:
    # Player's strength * Weapon's modifier * NPC defense modifier.
    # @param self a pointer to the current object.
    # @param target a NPC object, the current target of the attack.
    # @return The total damage inflicted by all weapons in the inventory to the
    #         NPC.
    ############################################################################
    def attack(self, target):
        total = 0
        for item in self.inventory: #Attack with all weapons in the inventory at once
            total += self.strength * item.getModifier() * target.getModifier(item.getName())
        return total

    ############################################################################
    # Decrease the Player's health by the damage value.
    # If the health reaches zero, the Player will let the Game know that the
    # game is over, and the user lost.
    # @param self a pointer to the current object.
    # @param damage the amount of health lost.
    ############################################################################
    def damage(self, damage):
        self.health -= damage
        if(self.health <= 0):
            for observer in self.observers:
                observer.update(True, "The player has lost!")

    ############################################################################
    # Decrease the durability of each Weapon in the Player's inventory by one.
    # @param self a pointer to the current object.
    ############################################################################
    def consumeAllWeapons(self):
        for weapon in self.inventory:
            weapon.consumeWeapon()

    ############################################################################
    # Reset the durability of all the Weapons in the Player's inventory.
    # @param self a pointer to the current object.
    ############################################################################
    def resetAllWeapons(self):
        for weapon in self.inventory:
            weapon.reset()

################################################################################
# A Person is a friendly NPC.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class Person(NPC):

    ############################################################################
    # A Person has 100 hp, heals the player for 1 hp by dealing -1 damage,and
    # cannot be damaged by the Player nor other NPCs.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        NPC.__init__(self, "Person", 100, -1, -1, False, {})

################################################################################
# A Zombie is an enemy NPC.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class Zombie(NPC):

    ############################################################################
    # A Zombie has between 50 and 100 hp, damages the player by a value
    # between 0 and 10 hp per attack, and receive double the damage by SourStraws.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        NPC.__init__(self, "Zombie", random.randint(50, 100), 0, 10, True, {"SourStraw": 2.0})

################################################################################
# A Vampire is an enemy NPC.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class Vampire(NPC):

    ############################################################################
    # A Vampire has between 100 and 200 hp, damages the player by a value
    # between 10 and 20 hp per attack, and is immune to ChocolateBars.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        NPC.__init__(self, "Vampire", random.randint(100, 200), 10, 20, True, {"ChocolateBar": 0.0} )

################################################################################
# A Ghoul is an enemy NPC.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class Ghoul(NPC):

    ############################################################################
    # A Ghoul has between 40 and 80 hp, damages the player by a value
    # between 15 and 30 hp per attack, and receive five times the damage
    # by NerdBombs.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        NPC.__init__( self, "Ghoul", random.randint(40, 80), 15, 30, True, {"NerdBomb": 5.0} )

################################################################################
# A Werewolf is an enemy NPC.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class Werewolf(NPC):

    ############################################################################
    # A Werewolf has 200 hp, damages the player by a value
    # between 0 and 40 hp per attack, and is immune to SourStraws and ChocolateBars.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        NPC.__init__(self, "Werewolf", 200, 0, 40, True, {"ChocolateBar": 0.0, "SourStraw": 0.0} )
