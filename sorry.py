from classes import *

def printIntroduction():
    # print an introduction
    pass

def printInstructions():
    # print instructions
    pass

def getNumberOfPlayers():
    pass

def getPlayerAge():
    pass

def gameOver():
    pass

def playSorryCard(card):
    pass

def playPlayingCard(card):
    pass

players = Players()

playingDeck = PlayingDeck()
sorryDeck = SorryDeck()

printIntroduction()
if raw_input("Do you want instructions? ").lower() == "y":
    printInstructions()
numPlayers = getNumberOfPlayers()
for i in range(numPlayers - 1):
    players.addPlayer(CompPlayer())
name = raw_input("What is your name? ")
age = getPlayerAge()
players.addPlayer(Player(name,age))
players.orderForPlay()
player = players.next()
while not gameOver(players):
    playingCard = playingDeck.draw()
    player.hand.addCard(playingCard)
    cardToPlay = player.getCardToPlay()
    if cardToPlay.getValue() == 0: # sorry value
        playingDeck.discard(cardToPlay)
        cardToPlay = sorryDeck.draw()
        playSorryCard(cardToPlay)
        sorryDeck.discard(cardToPlay)
        goAgain = False
    else:
        discard = raw_input("Would you like to discard this card? ")
        if discard:
            playingDeck.discard(cardToPlay)
        else:
            goAgain = playPlayingCard(cardToPlay)
    if not goAgain:
        player = players.next()

