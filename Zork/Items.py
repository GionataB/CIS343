import random

class Weapon(object):
    def __init__(self, name, minAttackModifier, maxAttackModifier, uses):
        self.name = name
        self.minAttackModifier = minAttackModifier
        self.maxAttackModifier = maxAttackModifier
        self.uses = uses
        self.maxUses = uses

    def getName(self):
        return self.name

    def canUse(self):
        return self.uses != 0 #return true if the weapon can be used, false otherwise

    def getModifier(self):
        if(self.canUse()):
            return random.randint(self.minAttackModifier, self.maxAttackModifier) / 100
        else:
            return 0 #The weapon does no damage

    def reset(self):
        self.uses = self.maxUses

    def consumeWeapon(self):
        if(self.canUse):
            self.uses -= 1

class HersheyKiss(Weapon):
    def __init__(self):
        Weapon.__init__(self, "HersheyKiss", 100, 100, -1)

class SourStraw(Weapon):
    def __init__(self):
        Weapon.__init__(self, "SourStraw", 100, 175, 2)

class ChocolateBar(Weapon):
    def __init__(self):
        Weapon.__init__(self, "ChocolateBar", 200, 240, 4)

class NerdBomb(Weapon):
    def __init__(self):
        Weapon.__init__(self, "NerdBomb", 350, 500, 1)
