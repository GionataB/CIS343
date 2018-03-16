################################################################################
# The World module contains classes that are used to build the game world.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################

import random
import observe
import characters

class House(observe.Observer, observe.Observable):

    def __init__(self):
        observe.Observable.__init__(self)
        self.totalNPCs = random.randint(1, 10) #The NPCs in the house, randomly chosen between 0 and 10
        self.NPCs = [] #The list of NPCs in the house
        randomNPC = 0
        for num in range(self.totalNPCs):
            randomNPC = random.randint(1, 5)
            if(randomNPC == 1):
                npc = characters.Person()
            elif(randomNPC == 2):
                npc = characters.Zombie()
            elif(randomNPC == 3):
                npc = characters.Vampire()
            elif(randomNPC == 4):
                npc = characters.Ghoul()
            elif(randomNPC == 5):
                npc = characters.Werewolf()
            npc.add_observer(self)
            self.NPCs.append(npc)
            randomNPC = 0

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
        self.NPCs[index] = characters.Person()
        self.NPCs[index].add_observer(self)
        if(self.checkEmpty()):
            for observer in self.observers:
                observer.update(False, "All monsters in the house defeated!\nYou found a chest full of weapons... All weapons' use have been reset!")

    def checkEmpty(self):
        for npc in self.NPCs:
            if(npc.getName() != "Person"):
                return False
        return True

    def getListMonster(self):
        return self.NPCs

class Neighborhood(observe.Observable):

    def __init__(self, rows, cols):
        observe.Observable.__init__(self)
        self.currentHouse = 0 #The house the player is in. Starts from zero.
        self.rows = rows #The number of houses in each column
        self.cols = cols #The number of houses in each row
        self.housesList = [] # A grid of Houses representing a real neighborhood
        for index in range(self.cols * self.rows):
            self.housesList.append(House())

    def showNeighborhood(self):
        for index in range(len(self.housesList)):
            if(index == 0):
                print("|", end=" ")
            elif(index % self.cols == 0):
                print("|")
                print("|", end=" ")
            if(index == self.currentHouse):
                print("~", end=" ")
            elif(index < self.currentHouse):
                print("O", end=" ")
            else:
                print("X", end=" ")
        else:
            print("|")

    def nextHouse(self):
        self.currentHouse += 1
        if(self.currentHouse >= len(self.housesList)):
            for observer in self.observers:
                observer.update(True, "The player wins!")
        elif(self.housesList[self.currentHouse].checkEmpty()):
            self.nextHouse()
        else:
            print("You enter a house!")

    def getCurrentHouse(self):
        return self.housesList[self.currentHouse]

    def getHouseList(self):
        return self.housesList
