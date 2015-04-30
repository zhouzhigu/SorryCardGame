from classes import *

# Brendan
def printIntroduction():
    print "Welcome to the Sorry Card Game"

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
