import zork

def pause(option):
    if option == "n":
        input("Press a button to continue...")

print("Welcome to Zork!")
row = int(input("How many rows do you want in the board?\n"))
column = int(input("How many columns do you want in the board?\n"))
game = zork.Game(row, column)
skipBattles = ""
while skipBattles != "y" and skipBattles != "n":
    skipBattles = input("Do you want to skip the battles and get the result for each house? (y/n)\n").lower()
print("The game will have a total of %u houses to visit.\n You are entering the first house!" % (row * column))
while game.getState():
    game.setPlayerTurn(False) #The player will always attack. If he defeats all the monsters in the house, the player should have another turn
    game.displayBoard()
    print("HP: %u" % game.getPlayerHealth())
    print("There are %u monsters in the house!" % game.getHouseInfo())
    pause(skipBattles)
    print("Your Turn!")
    game.playerTurn()
    pause(skipBattles)
    if not game.isPlayerTurn():
        print("Monsters Turn!")
        pause(skipBattles)
        game.npcTurn()
