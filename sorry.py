from classes import *

players = Players()

playingDeck = PlayingDeck()
sorryDeck = SorryDeck()
playingDiscardPile = Pile()
sorryDiscardPile = Pile()

printIntroduction()
if raw_input("Do you want instructions? ").lower() == "y":
    printInstructions()
numPlayers = 0
while not numPlayers:
    numPlayers = getPlayerNumber()
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
        playingDiscardPile.add(cardToPlay)
        cardToPlay = sorryDeck.draw()
        playSorryCard(cardToPlay)
        sorryDiscardPile.add(cardToPlay)
        goAgain = False
    else:
        discard = raw_input("Would you like to discard this card? ")
        if discard:
            playingDiscardPile.add(cardToPlay)
        else:
            goAgain = playPlayingCard(cardToPlay)
    if not goAgain:
        player = players.next()

