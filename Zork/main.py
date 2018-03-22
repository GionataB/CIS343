#!/usr/bin/env python3

import zork

################################################################################
# Puts a stop to the game and waits for an input before proceeding.
# At the beginning of the game, the user can choose if they want to play using
# these stops to check the battle reports or just go until the game is over.
# @param option option selected by the user.
################################################################################
def pause(option):
    if option == "n":
        input("Press enter to continue...")

print("Welcome to Zork!")
row = int(input("How many rows do you want in the board?\n"))
column = int(input("How many columns do you want in the board?\n"))
game = zork.Game(row, column) #Create the game
skipBattles = "" #The user can decide to not have interruptions during the game.
while skipBattles != "y" and skipBattles != "n":
    skipBattles = input("Do you want to skip the battles and get the result for each house? (y/n)\n").lower()
    if(skipBattles == "y"):
        input("You chose to fast forward the game to the end.\nA Battle report will still be made and can be read by scrolling up the screen.\nPress enter to continue...")
print("The game will have a total of %u houses to visit.\n You are entering the first house!" % (row * column))
while game.getState(): #From this point it's the actual body of the game, that iterates until the game's state is True.
    game.setPlayerTurn(False) #The player will always attack. If he defeats all the monsters in the house, the player should be first to attack in the next house.
    game.displayBoard() #Print the Houses as a grid.
    print("HP: %u" % game.getPlayerHealth()) #print info on the Player.
    if(game.getHouseInfo() == 1): #Make the output prettier by printing a different message with only one monster.
        print("There is %u monster in the house!" % game.getHouseInfo())
    else:
        print("There are %u monsters in the house!" % game.getHouseInfo())
    pause(skipBattles)
    print("Your Turn!")
    game.playerTurn() #The player's turn
    pause(skipBattles)
    if not game.isPlayerTurn():
        print("Monsters Turn!")
        game.npcTurn() #the NPC's turn.
        pause(skipBattles)
