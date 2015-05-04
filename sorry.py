from classes import *

# Brendan
def printIntroduction():
	# print an introduction
	pass

# Brendan
def printInstructions():
	# print instructions
	pass

# Brendan
def getNumberOfPlayers():
	pass

# Brendan
def getPlayerAge():
	pass

sorryGame = SorryGame()

printIntroduction()
if raw_input("Do you want instructions? ").lower()[0] == "y":
	printInstructions()
numPlayers = getNumberOfPlayers()
for i in range(numPlayers - 1):
	sorryGame.addPlayer(CompPlayer())
name = raw_input("What is your name? ")
age = getPlayerAge()
sorryGame.addPlayer(Player(name,age))
sorryGame.orderForPlay()
sorryGame.deal()
sorryGame.nextPlayer()
while not sorryGame.gameOver():
	sorryGame.move()
sorryGame.printResults()
