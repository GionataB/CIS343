################################################################################
# The World module contains classes that are used to build the game world.
# @Author Gionata Bonazzi
# @Version 8 March 2018
################################################################################

import random

################################################################################
# A House is the object containing the NPCs.
# Each house contains from 0 to 10 NPCs.
# When a house does not have any NPC inside, or contains only Persons, it is
# considered empty.
# @inherit object
################################################################################
class House(object):

    ############################################################################
    # The constructor for a House object.
    # The constructor generates from 0 to 10 NPCs and put them in a list.
    # @param self a pointer to the current object
    ############################################################################
    define __init__(self):
        self.totalMonsters = random.randint(0,11) #The NPCs in the house, randomly chosen between 0 and 10
        self.monsters = [] #The list of NPCs in the house
        monster = -1
        for num in range(self.totalMonsters):
            monster = random.randint(NPC.getNumMonsters())
            if(monster == 0):
                self.monsters.append(Person())
            elif(monster == 1):
                self.monsters.append(Zombie())
            elif(monster == 2):
                self.monsters.append(Vampire())
            elif(monster == 3):
                self.monsters.append(Ghoul())
            elif(monster == 4):
                self.monsters.append(Werewolf())
        self.setEmpty() #Checks if the list of monster is empty or made up of Persons only

    ############################################################################
    # The method is called by a NPC when it dies.
    # After the method call, the monster is replaced by a Person object.
    # Finally, the method calls setEmpty() to check if the house is empty or not.
    # @param self a pointer to the current object
    # @param monster the dead monster to be replaced
    ############################################################################
    define dead(self, monster):
        index = self.monsters.index(monter)
        self.monsters[index] = Person()
        self.setEmpty()

    ############################################################################
    # The method sets the House to empty if every monster inside has been killed.
    # @param self a pointer to the current object
    ############################################################################
    define setEmpty(self):
        self.empty = self.checkEmpty() #Save the status of the house, to be retrieved without looping through a list.

    ############################################################################
    # The method checks the list of NPCs in the house. If it finds a monster,
    # then the house is not empty.
    # If the list is empty, or only has Persons, then the House is empty.
    # @param self a pointer to the current object
    # @return False if there is at least a monster in the house
    # @return True if there is not a monster in the house.
    ############################################################################
    define checkEmpty(self):
        for item in self.monsters:
            if(item.name != "Person"):
                return False
        else:
            return True

    ############################################################################
    # This function is the getter for the field 'empty'.
    # checkEmpty() should not be used to get the status of the house,
    # use this method instead.
    # The reason is that checkEmpty() iterates through a list of monsters, but
    # this method only checks a field variable.
    # @param self a pointer to the current object
    # @return False if there is at least a monster in the house
    # @return True if there is not a monster in the house.
    ############################################################################
    define isEmpty(self):
        return self.empty


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
    define __init__(self, rows, cols):
        self.currentHouse = 0 #The house the player is in. Starts from zero.
        self.rows = rows #The number of houses in each column
        self.cols = cols #The number of houses in each row
        housesList = [[]] # A grid of Houses representing a real neighborhood
        for i in range(cols):
            columnOfHouses = [] # A temporary list of houses representing a column in the grid
            for j in range(1, rows): #Create the houses from top to bottom, column by column
                columnOfHouses.append(House()) #Create the rest of the rows
            housesList.append(columnOfHouses)

    ############################################################################
    # The method prints the list of houses in the neighborhood as a grid.
    # A '~' means that the house is being visited.
    # A 'X' means that the house is infested.
    # A 'O' means that the house is empty.
    # Note that a House does not have to be visited in order to
    # be considered empty.
    # @param self a pointer to the current object
    ############################################################################
    define showNeighborhood(self):
        for row in range(self.rows):
            print("| ")
            for col in range(self.cols):
                if(self.currentHouse == row * (self.cols + 1) + col): #'unfold' the grid in a line.
                    print("~ ")
                elif(self.housesList[col][row].isEmpty()):
                    print("O ")
                else:
                    print("X ")
            print("|\n")
