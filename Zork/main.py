def pause(option):
    if not option:
        raw_input("Press a button to continue...")

print("Welcome to Zork!")
row = input("How many rows do you want in the board?\n")
column = input("How many columns do you want in the board?\n")
game = Game(row, column)
skipBattles = ""
while skipBattles != "y" or skipBattles != "n":
    skipBattles = raw_input("Do you want to skip the battles and get the result for each house? (y/n)").lower()
print("The game will have a total of %u houses to visit.\n You are entering the first house!" % (row * column))
while game.getState():
    game.setPlayerTurn(False) #The player will always attack. If he defeats all the monsters in the house, the player should have another turn
    game.displayBoard()
    print("HP: %u" % player.getHealth())
    print("There are %u monsters in the house!" % game.getHouseInfo())
    pause(skipBattles)
    print("Your Turn!")
    game.playerTurn()
    pause(skipBattles)
    if not game.isPlayerTurn():
        print("Monsters Turn!")
        pause(skipBattles)
        game.npcTurn()
