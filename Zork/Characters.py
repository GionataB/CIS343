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

class NPC(Observable):

    ## The number of unique NPCs currently in the game ##
    numMonsters = 5

    def __init__(self, name, health, minDamage, maxDamage, canBeDamaged, modifier):
        Observable.__init__(self)
        self.name = name #The type of NPC
        self.health = health #The NPC's health
        self.minDamage = minDamage #The NPC's minimum damage it can deal
        self.maxDamage = maxDamage #The NPC's maximum damage it can deal
        self.canBeDamaged = canBeDamaged #Tells if the NPC is invincible or not
        self.modifier = modifier #A dictionary of weaknesses and immunities. They are both considered damage modifiers.

    def getNumMonsters(self):
        return self.numMonsters

    def attack(self):
        return random.randint(self.minDamage, self.maxDamage)

    def damage(self, damage):
        if(self.canBeDamaged): #Decrease the NPC's health only if it can be damaged.
            self.health -= damage #Inflict the damage
            if(self.health <= 0):
                for observer in self.observers:
                    observer.update(self) #Change the monster back to a person

    def getModifier(self, weaponName):
        if(self.modifier.has_key(weaponName)): #Check that the weapon is in the dictionary
            return self.modifier["name"]
        return 1.0 #The npc does not have a modifier for that weapon

class Player(Observable):

    def __init__(self):
        Observable.__init__(self)
        self.health = random.randint(100, 125) #The health value. The player loses when the health reaches 0 (or less)
        self.strength = random.randint(10, 20) #The raw strength. the damage inflicted is calculated using the raw strength multiplied by some modifiers
        self.inventory = [HersheyKiss()] #The inventory has to have at least one HersheyKiss
        weapon = 0 #Make sure that there is no error in the first random weapon
        for i in range(9): #Randomly choose the other 9 weapons
            weapon = random.randint(1, 4)
            if(weapon == 1):
                weaponList.append(HersheyKiss())
            elif(weapon == 2):
                weaponList.append(SourStraw())
            elif(weapon == 3):
                weaponList.append(ChocolateBar())
            elif(weapon == 4):
                weaponList.append(NerdBomb())

    def getHealth(self):
        return self.health

    def attack(self, target):
        total = 0
        for item in self.inventory: #Attack with all weapons in the inventory at once
            total += self.strength * item.getModifier() * target.getModifier(item.getName())
        return total

    def damage(self, damage):
        self.health -= damage
        if(self.health <= 0):
            for observer in self.observers:
                observer.update("The player has lost!")

    def consumeAllWeapons(self):
        for weapon in self.inventory:
            weapon.consumeWeapon()

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
