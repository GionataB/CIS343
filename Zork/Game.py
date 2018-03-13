import observe

class Game(Observer):
    def __init__(self, row, cols):
        self.playerTurn = True
        self.gameRunning = True
        self.player = Player()
        self.player.add_observer(self)
        self.neighborhood = Neighborhood(row, cols)
        self.neighborhood.add_observer(self)
        for house in self.neighborhood.getHouseList():
            self.house.add_observer(self)

    def displayBoard(self):
        self.neighborhood.showNeighborhood()

    def getHouseInfo(self):
        return self.neighborhood.getHouse.getNumMonsters()

    def isPlayerTurn(self):
        return self.playerTurn

    def setPlayerTurn(self, option):
        self.playerTurn = option

    def playerTurn(self):
        house = self.neighborhood.getCurrentHouse()
        for monster in house.getListMonster():
            attack = self.player.attack(monster)
            monster.damage(attack)
            print("You dealt %u damage to a %s" % (attack, monster.getName()))
        self.player.consumeAllWeapons()

    def npcTurn(self):
        total = 0
        house = self.neighborhood.getCurrentHouse()
        for npc in house.getListMonster():
            total += npc.attack
        print("Ouch! The monsters in the house attacked you for a total of %u damage!" % total)
        self.player.damage(total)

    def update(self):
        print("All monsters in the house defeated!\nYou found a chest full of weapons... All weapons' use have been reset!")
        self.neighborhood.nextHouse()
        self.player.resetAllWeapons()
        self.setPlayerTurn(True)

    def update(self, message):
        print(message)
        self.gameRunning = False

    def getState(self):
        return self.gameRunning
