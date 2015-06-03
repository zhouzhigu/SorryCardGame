from classes import *

def printIntroduction():
	print "Welcome to the Sorry Card Game"

def printInstructions():
	# print instructions
	print """
Object: Be the first person to flip over all your Start cards
Setup: Pick a blue, green, red or yellow card as your Start card and have them face down;
depending on the number of players. (4 players max)
Now, shuffle the playing cards and give four to each person playing
Then, shuffle the sorry cards and playing cards, and put them into two seperate piles.
Once that is done, you are ready to start the game. Youngest player goes first."""

	raw_input("press Enter")

	print """
On your turn: you must do two things:
1. draw a card
2. play a card, and discard it
Drawing a card: you must draw a card from the playing deck and put it in your hand.
Then you may proceed to play a card. If the card has a number on it, you may put it ontop
of your Start card. Your Start card must reach 15 before you can flip it. It cannot be over 15,
it must be 15. """

def getNumberOfPlayers():
	number, noNumber = 0, True
	while noNumber:
		number = raw_input("How many players are there? ")
		try:
			number = int(number)
			noNumber = False
		except:
			noNumber = True
		if number not in [2,3,4]:
			noNumber = True
	return number

def getPlayerAge():
	age, noAge = 0, True
	while noAge:
		age = raw_input("How are old are you? ")
		try:
			age = int(age)
			noAge = False
		except:
			noAge = True
	return age

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
"""
while not sorryGame.gameOver():
	sorryGame.move()
sorryGame.printResults()
"""

def demo():
    for player in sorryGame._players:
        print i, player, player.getName(), player.getAge()
    sorryGame.playingDeck.shuffle()
    card = sorryGame.playingDeck.draw()
    print card.getValue()
    print card.getInstructions()
