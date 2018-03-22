################################################################################
# The zork module contains game classes. Each game class combines all the elements
# in a set of rule to play a particular game. Right now there is only one type
# of game, with the rules defined for the project.
# @Author Gionata Bonazzi
# @Version 13 March 2018
################################################################################

import observe
import world
import characters

################################################################################
# A Game object contains an instance of a Player and Neighborhood object,
# making the two interact with each other under a set of rules that define a
# game.
# @Author Gionata Bonazzi
# @Version 13 March 2018
################################################################################
class Game(observe.Observer):

    ############################################################################
    # Constructor for a Game object, defining the field variables for the game.
    # Comments in the code will provide more documentation about the field
    # variables defined.
    # @param self a pointer to the current object.
    # @param row the number of rows in the grid that makes up the neighborhood
    # @param col the number of columns in the grid that makes up the neighborhood
    ############################################################################
    def __init__(self, row, col):
        self.pTurn = True #True if it is the Player's turn, false otherwise
        self.gameRunning = True #True if the Game is running, false it has reached a state where it should stop.
        self.player = characters.Player() #The user's avatar in the game.
        self.player.add_observer(self) #The Game observes the Player.
        self.neighborhood = world.Neighborhood(row, col) #The world where the game takes place.
        self.neighborhood.add_observer(self) #The Game observes the Neighborhood.
        for house in self.neighborhood.getHouseList():
            house.add_observer(self)

    ############################################################################
    # Get method to access the Player's health.
    # @param self a pointer to the current object.
    # @return the Player's health.
    ############################################################################
    def getPlayerHealth(self):
        return self.player.getHealth()

    ############################################################################
    # Get method to access the Neighborhood's function that displays the houses
    # as a matrix.
    # @param self a pointer to the current object.
    ############################################################################
    def displayBoard(self):
        self.neighborhood.showNeighborhood()

    ############################################################################
    # Get the number of non-Person NPCs in the current House.
    # @param self a pointer to the current object.
    # @return the number of monsters in the current House.
    ############################################################################
    def getHouseInfo(self):
        return self.neighborhood.getCurrentHouse().getNumMonsters()

    ############################################################################
    # Get who is playing the current turn, the Player or the NPCs.
    # @param self a pointer to the current object.
    # @return True if it is the Player's turn, false otherwise.
    ############################################################################
    def isPlayerTurn(self):
        return self.pTurn

    ############################################################################
    # Set the pTurn variable to the "option" value.
    # @param self a pointer to the current object.
    # @param option the new value to be assigned.
    ############################################################################
    def setPlayerTurn(self, option):
        self.pTurn = option

    ############################################################################
    # The method contains all the actions done when it is the Player's turn.
    # @param self a pointer to the current object.
    ############################################################################
    def playerTurn(self):
        house = self.neighborhood.getCurrentHouse()
        for monster in house.getListMonster():
            attack = self.player.attack(monster)
            if(monster.canBeDamaged()):
                print("You dealt %u damage to a %s" % (attack, monster.getName()))
            monster.damage(attack)
        self.player.consumeAllWeapons() #Consume the weapons after all monsters have been hit.

    ############################################################################
    # The method contains all the actions done when it is the NPC's turn.
    # @param self a pointer to the current object.
    ############################################################################
    def npcTurn(self):
        total = 0
        house = self.neighborhood.getCurrentHouse()
        for npc in house.getListMonster():
            total += npc.attack()
        if(total > 0):
            print("Ouch! The monsters in the house attacked you for a total of %u damage!" % total)
        elif(total < 0):
            print("The people in the house healed you for a total of %u health points!" % (total * -1))
        else:
            print("You avoided being damaged!")
        self.player.damage(total)

    ############################################################################
    # When there is a change in a House, or in the Player, the Game will
    # print a corresponding message. If gameOver is False, it means that the
    # Player is alive and that the current House is empty. First, play a turn in
    # the current house, so that the Player gets healed a bit, then go to the
    # next House and, if there are more Houses in the Neighborhood left, reset
    # the Weapons in the player inventory and set the current turn to the
    # Player's.
    # @param self a pointer to the current object.
    # @param gameOver True if the Player is dead, or all the Houses in the
    #           Neighborhood have been freed, false otherwise.
    # @param message a message to be printed.
    ############################################################################
    def update(self, gameOver, message):
        print(message)
        if(not gameOver):# If the game is not over
            self.npcTurn() #Make sure the player is healed by all the people in the house.
            self.neighborhood.nextHouse()
            self.player.resetAllWeapons()
            self.setPlayerTurn(True)
        self.gameRunning = not gameOver # the game runs when the game is not over, so they are the opposite from each other.

    ############################################################################
    # Get the state of the game.
    # @param self a pointer to the current object.
    # @return True if the game is still running, False if it should stop.
    ############################################################################
    def getState(self):
        return self.gameRunning
