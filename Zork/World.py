################################################################################
# The World module contains classes that are used to build the game world.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################

import random
import observe

class House(Observer, Observable):

    def __init__(self):
        Observable.__init__(self)
        self.totalNPCs = random.randint(0,11) #The NPCs in the house, randomly chosen between 0 and 10
        self.NPCs = [] #The list of NPCs in the house
        randomNPC = -1
        for num in range(self.totalMonsters):
            randomNPC = random.randint(NPC.getNumMonsters())
            if(randomNPC == 0):
                npc = Person()
            elif(randomNPC == 1):
                npc = Zombie()
            elif(randomNPC == 2):
                npc = Vampire()
            elif(randomNPC == 3):
                npc = Ghoul()
            elif(randomNPC == 4):
                npc = Werewolf()
            self.NPCs.append(npc)
            npc.add_observer(self)

    def getNumMonsters(self):
        total = 0
        for npc in self.NPCs:
            if(npc.getName() != "Person"):
                total += 1
        return total

    def update(self, monster):
        print("You defeated a %s!" % monster.getName())
        index = self.NPCs.index(monster)
        monster.remove_observer(self)
        self.NPCs[index] = Person()
        self.monster[index].add_observer()
        if(self.checkEmpty()):
            for observer in self.observers:
                observer.update()

    def checkEmpty(self):
        for item in self.NPCs:
            if(item.name != "Person"):
                return False
        else:
            return True

    def getListMonster(self):
        return self.NPCs

class Neighborhood(Observable):

    def __init__(self, rows, cols):
        Observable.__init__()
        self.currentHouse = 0 #The house the player is in. Starts from zero.
        self.rows = rows #The number of houses in each column
        self.cols = cols #The number of houses in each row
        self.housesList = [] # A grid of Houses representing a real neighborhood
        for index in range(self.cols * self.rows):
            self.housesList.append(House())

    def showNeighborhood(self):
        for index in range(len(self.housesList)):
            if(index % self.cols == 0):
                print(" |")
                print("|", end=" ")
            else if(index == self.currentHouse):
                print("~", end=" ")
            else if(index < self.currentHouse):
                print("O", end=" ")
            else:
                print("X", end=" ")

    def nextHouse(self):
        self.currentHouse += 1
        if(self.housesList[self.currentHouse].checkEmpty):
            self.nextHouse()
        if(self.currentHouse >= len(self.housesList)):
            for observer in self.observers:
                observer.update("The player wins!")
        else:
            print("You enter a house!")

    def getCurrentHouse(self):
        return self.housesList[self.currentHouse]

    def getHouseList(self):
        return self.housesList
