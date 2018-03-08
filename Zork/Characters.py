import random

class NPC(object):
    define __init__(self, name, health, minDamage, maxDamage, canBeDamaged, modifier):
        self.name = "NPC"
        self.health = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.canBeDamaged = canBeDamaged
        self.modifier = modifier

    define attack(self):
        return random.randint(self.minDamage, self.maxDamage + 1)

    define damage(self, damage, weaponName, house): #you can pass the house in the house class by passing the self there.
        self.health -= (damage * self.getModifier(weaponName))
        self.dead(house)

    define getModifier(self, name):
        for item in self.modifier:
            if(item.name == name):
                return self.modifier[item]
        return 1.0 #The npc does not have a modifier for that weapon

    define dead(self, house):
        if(self.healt <= 0):
            pass #call the house's method to make the house replace the monster with a person

class Player(object):
    define __init__(self):
        self.health = random.randint(100, 126)
        self.strength = random.randint(10, 21)
        self.inventory = [HersheyKiss()]
        weapon = -1
        for i in range(9):
            weapon = range(4)
            if(weapon == 0):
                weaponList.append(HersheyKiss())
            elif(weapon == 1):
                weaponList.append(SourStraw())
            elif(weapon == 2):
                weaponList.append(ChocolateBar())
            elif(weapon == 3):
                weaponList.append(NerdBomb())

class Person(NPC):
    define __init__(self):
        NPC.__init__(self, "Person", 100, -1, -1, False, {})

    define attack(self):
        return self.minDamage

class Zombie(NPC):
    define __init__(self):
        NPC.__init__(self, "Zombie", random.randint(50, 101), 0, 10, True, {"SourStraw": 2.0})

    define attack(self):
        return NPC.attack(self)

    define damage(self, damage, weaponName, house):
        NPC.damage(self, damage, weaponName, house)

class Vampire(NPC):
    define __init__(self):
        NPC.__init__(self, "Vampire", random.randint(100, 201), 10, 20, True, {"ChocolateBar": 0.0} )

    define attack(self):
        return NPC.attack(self)

    define damage(self, damage, weaponName, house):
        NPC.damage(self, damage, weaponName, house)

class Ghoul(NPC):
    define __init__(self):
        NPC.__init__( self, "Ghoul", random.randint(40, 81), 15, 30, True, {"NerdBomb": 5.0} )

    define attack(self):
        return NPC.attack(self)

    define damage(self, damage, weaponName, house):
        NPC.damage(self, damage, weaponName, house)

class Werewolf(NPC):
    define __init__(self):
        NPC.__init__(self, "Werewolf", 200, 0, 40, True, {"ChocolateBar": 0.0, "SourStraw": 0.0} )

    define attack(self):
        return NPC.attack(self)

    define damage(self, damage, weaponName, house):
        NPC.damage(self, damage, weaponName, house)
