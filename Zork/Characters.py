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

################################################################################
# A NPC is an object for a non-playable character.
# A NPC can be either friendly, or not. Each NPC has a health value, an attack
# power, and some weaknesses or immunities.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class NPC(Observable):

    ## The number of unique NPCs currently in the game ##
    numMonsters = 5

    ############################################################################
    # Contructor for a NPC object. When a NPC is created, the constructor
    # records the type of NPC, its healt, its damage (between minDamage, maxDamage)
    # and a dictionary of immunities.
    # It is also recorded a variable that tells the program if that NPC should
    # be damaged or not. An example is a person, a friendly NPC that is not
    # damaged by the player.
    # @param self a pointer to the current object.
    # @param name the type of NPC created.
    # @param health the health of the monster.
    # @param minDamage the minimum damage the NPC can inflict.
    # @param maxDamage the maximum damage the NPC can inflict.
    # @param canBeDamaged variable telling the program if the NPC can be damaged.
    # @param modifier a dictionary of weaknesses and immunities to different weapons.
    #                 if the NPC does not have any modifier, an empty dictionary will be passed.
    ############################################################################
    def __init__(self, name, health, minDamage, maxDamage, canBeDamaged, modifier):
        Observable.__init__(self)
        self.name = name #The type of NPC
        self.health = health #The NPC's health
        self.minDamage = minDamage #The NPC's minimum damage it can deal
        self.maxDamage = maxDamage #The NPC's maximum damage it can deal
        self.canBeDamaged = canBeDamaged #Tells if the NPC is invincible or not
        self.modifier = modifier #A dictionary of weaknesses and immunities. They are both considered damage modifiers.


    ############################################################################
    # Method to retrieve a field value.
    # The number of monsters is a value that let the NPC class know how many
    # classes in the game inherit NPC.
    # @param self a pointer to the current object.
    # @return the number of unique monsters in the game.
    ############################################################################
    def getNumMonsters(self):
        return self.numMonsters

    ############################################################################
    # The method randomly choose an attack value between the NPC's minimum damage,
    # and its maximum.
    # @param self a pointer to the current object.
    # @return an attack value.
    ############################################################################
    def attack(self):
        return random.randint(self.minDamage, self.maxDamage + 1)

    ############################################################################
    # Decrease the NPC's health by an amount equal to the damage received.
    # If the NPC's health reaches zero (or less), it notifies the house the
    # NPC is in to replace it with a Person.
    # @param self a pointer to the current object.
    # @param damage the damage received.
    # @param house the House object the NPC is in.
    ############################################################################
    def damage(self, damage):
        if(self.canBeDamaged): #Decrease the NPC's health only if it can be damaged.
            self.health -= damage #Inflict the damage
            if(self.health <= 0):
                for observer in self.observers:
                    observer.update(self) #Change the monster back to a person

    ############################################################################
    # Method to retrieve a field value.
    # The method checks the dictionary of weaknesses and immunities,
    # and retrieves the correct damage modifier for that weapon on the NPC.
    # @param self a pointer to the current object.
    # @param weaponName the type of weapon used to deal damage.
    # @return a zero or positive float that is not equal to 1.0 if the weapon
    #         type is in the dictionary, 1.0 if it is not.
    ############################################################################
    def getModifier(self, weaponName):
        if(self.modifier.has_key(weaponName)): #Check that the weapon is in the dictionary
            return self.modifier["name"]
        return 1.0 #The npc does not have a modifier for that weapon

################################################################################
# A Player is the user's character in the game.
# The user loses the game if the Player dies.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class Player(object): #FIXME: an observer here for weapons.

    ############################################################################
    # Constructor for a Player object.
    # A Player has a health value randomly chosen between 100 and 125 (inclusive),
    # a strength value randomly chosen between 10 and 20,
    # and an inventory of items.
    # The inventory contains only 10 items, and the only items in the game are
    # weapons. One inventory slot is occupied by a HersheyKiss, a weapon that
    # never gets consumed. The remaining 9 weapons are randomly chosen.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        self.health = random.randint(100, 126) #The health value. The player loses when the health reaches 0 (or less)
        self.strength = random.randint(10, 21) #The raw strength. the damage inflicted is calculated using the raw strength multiplied by some modifiers
        self.inventory = [HersheyKiss()] #The inventory has to have at least one HersheyKiss
        weapon = -1 #Make sure that there is no error in the first random weapon
        for i in range(9): #Randomly choose the other 9 weapons
            weapon = random.randint(0, 4)
            if(weapon == 0):
                weaponList.append(HersheyKiss())
            elif(weapon == 1):
                weaponList.append(SourStraw())
            elif(weapon == 2):
                weaponList.append(ChocolateBar())
            elif(weapon == 3):
                weaponList.append(NerdBomb())

    ############################################################################
    # Calculate the damage to inflict to a NPC.
    # The damage formula is the raw strength * the item's damage modifier *
    # the NPC's damage modifier.
    # @param self a pointer to the current object.
    # @param npc the NPC currently targeted.
    # @return the total damage to inflict to the enemy.
    ############################################################################
    def attack(self, npc):
        total = 0
        for item in self.inventory: #Attack with all weapons in the inventory at once
            total += self.strength * item.getModifier() * npc.getModifier(item.getName())
        return total

    ############################################################################
    # When the player is attacked, decreases its life and tells the game if
    # the player is still alive.
    # @param self a pointer to the current object.
    # @param damage the damage received by the player.
    # @return True if the player is dead, False otherwise.
    ############################################################################
    def damage(self, damage):
        self.health -= damage
        if(self.health <= 0):
            return True
        else:
            return False

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
        NPC.__init__(self, "Zombie", random.randint(50, 101), 0, 10, True, {"SourStraw": 2.0})

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
        NPC.__init__(self, "Vampire", random.randint(100, 201), 10, 20, True, {"ChocolateBar": 0.0} )

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
        NPC.__init__( self, "Ghoul", random.randint(40, 81), 15, 30, True, {"NerdBomb": 5.0} )

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
