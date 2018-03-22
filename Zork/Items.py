################################################################################
# The items module defines all objects used by the player that could be defined
# as usable items. The game in its current form has only weapons, but could
# be expanded with potion-like items to recover hp.
################################################################################

import random

################################################################################
# A Weapon object is an item used by the player to inflict damage to monsters.
# Each weapon has its own unique attack modifier, name, and how many times can be
# used.
# @Author Gionata Bonazzi
# @Version 15 March 2018
################################################################################
class Weapon(object):

    ############################################################################
    # Constructor for a Weapon object. Each Weapon has a name, an attack modifier
    # randomly selected between two numbers, and how many times the weapon can
    # be used.
    # @param self a pointer to the current object.
    # @param name the name of the weapon.
    # @param minAttackModifier the lower boundary for the attack modifier.
    # @param maxAttackModifier the higher boundary for the attack modifier.
    # @param uses The number of times a weaponn can be used.
    ############################################################################
    def __init__(self, name, minAttackModifier, maxAttackModifier, uses):
        self.name = name
        self.minAttackModifier = minAttackModifier
        self.maxAttackModifier = maxAttackModifier
        self.uses = uses
        self.maxUses = uses

    ############################################################################
    # Get the name of the weapon.
    # @param self a pointer to the current object.
    # @return the name of the weapon.
    ############################################################################
    def getName(self):
        return self.name

    ############################################################################
    # Checks if the weapon can be used. Generally, a Weapon can't be used if its
    # durability reaches zero. However, a Weapon like HersheyKiss does not have
    # durability, so "infinity" is emulated by using a negative number. Thus,
    # the only case a Weapon can't be used is when it reaches 0, assuming that
    # a Weapon that starts with a positive durability won't ever go lower than
    # zero.
    # @param self a pointer to the current object.
    # @return True if the Weapon can be used, False otherwise.
    ############################################################################
    def canUse(self):
        return self.uses != 0 #return true if the weapon can be used, false otherwise

    ############################################################################
    # Get the modifier of the weapon. If the weapon can be used, the modifire is
    # a randomly chosen number N such that N is a float with only two decimal
    # places, and N >= 0.00
    # @param self a pointer to the current object.
    # @return the weapon's attack modifier.
    ############################################################################
    def getModifier(self):
        if(self.canUse()):
            return float(random.randint(self.minAttackModifier, self.maxAttackModifier) / 100) #Implicit casting to a float with 2 decimal places.
        else:
            return 0 #The weapon does no damage

    ############################################################################
    # Restore the Weapon's durability.
    # @param self a pointer to the current object.
    ############################################################################
    def reset(self):
        self.uses = self.maxUses

    ############################################################################
    # Decreases the Weapon's durability by one, only if the Weapon can be used.
    # A special case is HersheyKiss, by the game's rule it does not have a
    # durablity, but in the program it has a negative value that keeps decreasing.
    # This is safe only because the durability gets reset after each House.
    # If they do not get reset, the durability could, in time, reach an
    # out-of-bounds negative value (impossible with the current game's rules).
    # @param self a pointer to the current object.
    ############################################################################
    def consumeWeapon(self):
        if(self.canUse):
            self.uses -= 1

################################################################################
# A HersheyKiss is a type of Weapon.
# @Author Gionata Bonazzi
# @Version 15 March 2018
################################################################################
class HersheyKiss(Weapon):

    ############################################################################
    # Constructor for a HersheyKiss object. A HersheyKiss has no damage modifier,
    # and no durability.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        Weapon.__init__(self, "HersheyKiss", 100, 100, -1)

################################################################################
# A SourStraw is a type of Weapon.
# @Author Gionata Bonazzi
# @Version 15 March 2018
################################################################################
class SourStraw(Weapon):

    ############################################################################
    # Constructor for a SourStraw object. A SourStraw has a damage modifier
    # randomly chosen between 1.0x and 1.7x increased damage, and can be used 2
    # times.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        Weapon.__init__(self, "SourStraw", 100, 175, 2)

################################################################################
# A ChocolateBar is a type of Weapon.
# @Author Gionata Bonazzi
# @Version 15 March 2018
################################################################################
class ChocolateBar(Weapon):

    ############################################################################
    # Constructor for a ChocolateBar object. A ChocolateBar has a damage modifier
    # randomly chosen between 2.0x and 2.4x increased damage, and can be used 4
    # times.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        Weapon.__init__(self, "ChocolateBar", 200, 240, 4)

################################################################################
# A NerdBomb is a type of Weapon.
# @Author Gionata Bonazzi
# @Version 15 March 2018
################################################################################
class NerdBomb(Weapon):

    ############################################################################
    # Constructor for a NerdBomb object. A NerdBomb has a damage modifier
    # randomly chosen between 3.5x and 5.0x increased damage, and can be used 1
    # time.
    # @param self a pointer to the current object.
    ############################################################################
    def __init__(self):
        Weapon.__init__(self, "NerdBomb", 350, 500, 1)
