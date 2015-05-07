from classes import *

# Brendan
def printIntroduction():
    print "Welcome to the Sorry Card Game"

# Brendan
def printInstructions():
    # print instructions
    print """
Object: Be the first person to flip over all your Start cards
Setup: Pick a blue, green, red or yellow card as your Start card and have them face down; 
depending on the number of players. (4 players max) 
Now, shuffle the playing cards and give four to each person playing
Then, shuffle the sorry cards and playing cards, and put them into two seperate piles.
Once that is done, you are ready to start the game. Youngest player goes first."""

""" 
raw_input("press Enter")

print """
On your turn: you must do two things:
1. draw a card
2. play a card, and discard it
Drawing a card: you must draw a card from the playing deck and put it in your hand. 
Then you may proceed to play a card. If the card has a number on it, you may put it ontop 
of your Start card. Your Start card must reach 15 before you can flip it. It cannot be over 15,
it must be 15. 

"""


# Brendan
def getNumberOfPlayers():
    print 
	"How many players?"

# Brendan
def getPlayerAge():
    print 
	"How old is the player"

sorryGame = SorryGame()

playingDeck = PlayingDeck()
sorryDeck = SorryDeck()

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
player = sorryGame.next()
while not sorryGame.gameOver():
    playingCard = playingDeck.draw()
    player.addCardToHand(playingCard)
    cardToPlay = player.choosePlay()
    if cardToPlay.getValue() == 0: # sorry value
        playingDeck.discard(cardToPlay)
        cardToPlay = sorryDeck.draw()
        sorryGame.playSorryCard(cardToPlay)
        sorryDeck.discard(cardToPlay)
        goAgain = False
    else:
        discard = raw_input("Would you like to discard this card? ")
        if discard:
            playingDeck.discard(cardToPlay)
        else:
            goAgain = sorryGame.playPlayingCard(cardToPlay)
    if not goAgain:
        player = game.next()

sorryGame.printResults()
