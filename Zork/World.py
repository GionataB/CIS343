################################################################################
# The World module contains classes that are used to build the game world.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################

import random
import observe
import characters

################################################################################
# A House is a container for NPCs.
# It inherits from Observer and Observable.
# It observes the NPCs contained in the House, and is observed by the Game.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class House(observe.Observer, observe.Observable):

    ############################################################################
    # A House contains between 1 to 10 NPCs.
    # @param self a pointer to the current object.
    ############################################################################
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

    ############################################################################
    # Finds the number of NPC that are "monsters". A monter is a NPC other than
    # a person.
    # @param self a pointer to the current object.
    # @return the number of non-Person NPCs.
    ############################################################################
    def getNumMonsters(self):
        total = 0
        for npc in self.NPCs:
            if(npc.getName() != "Person"):
                total += 1
        return total

    ############################################################################
    # When a NPC dies, this method replaces it with a Person.
    # If there are no monsters in the House left, it will let the Game know that
    # this House is "empty".
    # @param self a pointer to the current object.
    # @param monster the NPC to be replaced with a Person.
    ############################################################################
    def update(self, monster):
        print("You defeated a %s!" % monster.getName())
        index = self.NPCs.index(monster)
        monster.remove_observer(self)
        self.NPCs[index] = characters.Person()
        self.NPCs[index].add_observer(self)
        if(self.checkEmpty()):
            for observer in self.observers:
                observer.update(False, "All monsters in the house defeated!\nYou found a chest full of weapons... All weapons' use have been reset!")

    ############################################################################
    # Iterate through the list of NPCs to find if there are monsters left alive.
    # @param self a pointer to the current object.
    # @return True if there NPCs in the house are all Persons, False otherwise.
    ############################################################################
    def checkEmpty(self):
        for npc in self.NPCs:
            if(npc.getName() != "Person"):
                return False
        return True

    ############################################################################
    # Access the list of NPCs in the House.
    # @param self a pointer to the current object.
    # @return a list of NPCs.
    ############################################################################
    def getListMonster(self):
        return self.NPCs

################################################################################
# A Neighborhood is a container for Houses.
# It inherits from Observable.
# It is observed by the Game.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################
class Neighborhood(observe.Observable):

    ############################################################################
    # A Neighborhood contains rows * cols Houses.
    # the Neighborhood keeps track of the House being visited and a list of all
    # Houses (empty or not).
    # A Neighborhood can be thought as a matrix where each cell is a House.
    # @param self a pointer to the current object.
    # @param rows number of Houses in a column.
    # @param cols number of Houses in a row.
    ############################################################################
    def __init__(self, rows, cols):
        observe.Observable.__init__(self)
        self.currentHouse = 0 #The house the player is in. Starts from zero.
        self.rows = rows #The number of houses in each column
        self.cols = cols #The number of houses in each row
        self.housesList = [] # A grid of Houses representing a real neighborhood
        for index in range(self.cols * self.rows):
            self.housesList.append(House())

    ############################################################################
    # Display the list of Houses in a grid. Each House can be represented with a
    # symbol:
    # X is a House not visited, it can either be empty or not.
    # O is a House that has been visited, and thus it's "empty".
    # ~ is the House the Player is currently in.
    # @param self a pointer to the current object.
    ############################################################################
    def showNeighborhood(self):
        for index in range(len(self.housesList)):
            if(index == 0): #First, start with the Neighborhood "wall".
                print("|", end=" ")
            elif(index % self.cols == 0):
                print("|") #Put a wall at the end, and go to a new line
                print("|", end=" ") #Start the new line with a wall.
            if(index == self.currentHouse):
                print("~", end=" ")
            elif(index < self.currentHouse):
                print("O", end=" ")
            else:
                print("X", end=" ")
        else:
            print("|") #Finally, put the last wall.

    ############################################################################
    # Increase the currentHouse counter by one. If the counter is greater than
    # the number of Houses in the list, it means that the Player completed the
    # game.
    # If a House does not contain monsters, the Player will skip it.
    # @param self a pointer to the current object.
    ############################################################################
    def nextHouse(self):
        self.currentHouse += 1
        if(self.currentHouse >= len(self.housesList)):
            for observer in self.observers:
                observer.update(True, "The player wins!")
        elif(self.housesList[self.currentHouse].checkEmpty()):
            self.nextHouse()
        else:
            print("You enter a house!")

    ############################################################################
    # Get the current House.
    # @param self a pointer to the current object.
    # @return the House object the Player is currently in.
    ############################################################################
    def getCurrentHouse(self):
        return self.housesList[self.currentHouse]

    ############################################################################
    # Get the list of Houses in the Neighborhood
    # @param self a pointer to the current object.
    # @return a list of Houses.
    ############################################################################
    def getHouseList(self):
        return self.housesList
