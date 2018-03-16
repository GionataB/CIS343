import observe
import world
import characters

class Game(observe.Observer):
    def __init__(self, row, cols):
        self.pTurn = True
        self.gameRunning = True
        self.player = characters.Player()
        self.player.add_observer(self)
        self.neighborhood = world.Neighborhood(row, cols)
        self.neighborhood.add_observer(self)
        for house in self.neighborhood.getHouseList():
            house.add_observer(self)

    def getPlayerHealth(self):
        return self.player.getHealth()

    def displayBoard(self):
        self.neighborhood.showNeighborhood()

    def getHouseInfo(self):
        return self.neighborhood.getCurrentHouse().getNumMonsters()

    def isPlayerTurn(self):
        return self.pTurn

    def setPlayerTurn(self, option):
        self.pTurn = option

    def playerTurn(self):
        house = self.neighborhood.getCurrentHouse()
        for monster in house.getListMonster():
            attack = self.player.attack(monster)
            if(monster.canBeDamaged()):
                print("You dealt %u damage to a %s" % (attack, monster.getName()))
            monster.damage(attack)
        self.player.consumeAllWeapons()

    def npcTurn(self):
        total = 0
        house = self.neighborhood.getCurrentHouse()
        for npc in house.getListMonster():
            total += npc.attack()
        print("Ouch! The monsters in the house attacked you for a total of %u damage!" % total)
        self.player.damage(total)

    def update(self, gameOver, message):
        print(message)
        if(not gameOver):
            self.neighborhood.nextHouse()
            self.player.resetAllWeapons()
            self.setPlayerTurn(True)
        self.gameRunning = not gameOver

    def getState(self):
        return self.gameRunning
