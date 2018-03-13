################################################################################
# The World module contains classes that are used to build the game world.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################

import random
import observe

################################################################################
# A House is the object containing the NPCs.
# Each house contains from 0 to 10 NPCs.
# When a house does not have any NPC inside, or contains only Persons, it is
# considered empty.
# @inherit object
################################################################################
class House(Observer, Observable):

    ############################################################################
    # The constructor for a House object.
    # The constructor generates from 0 to 10 NPCs and put them in a list.
    # @param self a pointer to the current object
    ############################################################################
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
        self.setEmpty() #Checks if the list of monster is empty or made up of Persons only

    ############################################################################
    # The method is called by a NPC when it dies.
    # After the method call, the monster is replaced by a Person object.
    # Finally, the method calls setEmpty() to check if the house is empty or not.
    # @param self a pointer to the current object
    # @param monster the dead monster to be replaced
    ############################################################################
    def update(self, monster):
        index = self.NPCs.index(monster)
        monster.remove_observer(self)
        self.NPCs[index] = Person()
        self.monster[index].add_observer()
        for observer in self.observers:
            observer.update()
        self.setEmpty()

    ############################################################################
    # The method sets the House to empty if every monster inside has been killed.
    # @param self a pointer to the current object
    ############################################################################
    def setEmpty(self):
        self.empty = self.checkEmpty() #Save the status of the house, to be retrieved without looping through a list.

    ############################################################################
    # The method checks the list of NPCs in the house. If it finds a monster,
    # then the house is not empty.
    # If the list is empty, or only has Persons, then the House is empty.
    # @param self a pointer to the current object
    # @return False if there is at least a monster in the house
    # @return True if there is not a monster in the house.
    ############################################################################
    def checkEmpty(self):
        for item in self.NPCs:
            if(item.name != "Person"):
                return False
        else:
            return True

    ############################################################################
    # This function is the getter for the field 'empty'.
    # checkEmpty() should not be used to get the status of the house,
    # use this method instead.
    # The reason is that checkEmpty() iterates through a list of NPCs, but
    # this method only checks a field variable.
    # @param self a pointer to the current object
    # @return False if there is at least a monster in the house
    # @return True if there is not a monster in the house.
    ############################################################################
    def isEmpty(self):
        return self.empty

    def getNumMonsters(self):
        total = 0
        for npc in self.NPCs:
            if(npc.getName() != "Person"):
                total += 1
        return total

################################################################################
# A Neighborhood is the grid of houses were the game is played.
# The number of houses in a neighborhood is equal to rows * cols, the parameter
# passed to the constructor.
# @inherit object
################################################################################
class Neighborhood(object):

    ############################################################################
    # The constructor for a Neighborhood object.
    # The constructor creates a list made up of houses.
    # The list is arranged in a grid, each element of the list is a list of
    # houses (which is a list of all the houses in the column)
    # @param self a pointer to the current object
    # @param rows the number of houses in each column
    # @param cols the number of houses in each row
    ############################################################################
    def __init__(self, rows, cols):
        self.currentHouse = 0 #The house the player is in. Starts from zero.
        self.rows = rows #The number of houses in each column
        self.cols = cols #The number of houses in each row
        self.housesList = [] # A grid of Houses representing a real neighborhood
        for col in range(cols):
            for row in range(rows): #Create the houses from top to bottom, column by column
                housesList.append(House())
        self.totalMonsters()

    def totalMonsters(self):
        self.totalMonsters = 0
        for house in housesList:
            self.totalMonsters += house.getNumMonsters()

    def decreaseTotalMonsters(self):
        self.totalMonsters -= 1

    def getTotalMonsters(self):
        return self.totalMonsters

    ############################################################################
    # The method prints the list of houses in the neighborhood as a grid.
    # A '~' means that the house is being visited.
    # A 'X' means that the house is infested.
    # A 'O' means that the house is empty.
    # Note that a House does not have to be visited in order to
    # be considered empty.
    # @param self a pointer to the current object
    ############################################################################
    def showNeighborhood(self):
        for index in range(len(self.housesList)):
            if(index % self.cols == 0):
                print(" |")
                print("| "),
            else if(index == self.currentHouse):
                print("~ "),
            else if(self.housesList[index].isEmpty()):
                print("O "),
            else:
                print("X "),

    ############################################################################
    # Go to the next House.
    # @param self a pointer to the current object
    ############################################################################
    def nextHouse(self):
        self.currentHouse += 1

    ############################################################################
    # Get the current House object
    # @param self a pointer to the current object
    # @return the House object the player is currently in.
    ############################################################################
    def getHouse(self):
        return self.housesList[index]
