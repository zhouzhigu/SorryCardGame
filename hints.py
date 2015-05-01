"""
This logic was moved here so you could borrow from it
but it should be edited a lot
"""

playingCard = playingDeck.draw()
player.addCardToHand(playingCard)
goAgain, cardToDiscard = sorryGame.move()
if cardToDiscard:
    playingDeck.discard(cardToDiscard)
if not goAgain:
    player = sorryGame.nextPlayer()

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

