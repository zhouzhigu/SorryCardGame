import random

card_deck = ['1', '1', '1', '1', '2: Go again', '2: Go again', '2: Go again', '2: Go again', '3: Take a card from an opponents hand',
						  '3: Take a card from an opponents hand', '3: Take a card from an opponents hand', '4: You must discard a card to play this one',
						  '4: You must discard a card to play this one', '4: You must discard a card to play this one', '5', '5', '5', '7: Remove and discard the top card from an opponents deck',
						  '7: Remove and discard the top card from an opponents deck', '7: Remove and discard the top card from an opponents deck', '8', '8', '8', '10 or -1', '10 or -1', '10 or -1',
						  '11: You must play this card or discard it to trade hands', '11: You must play this card or discard it to trade hands', '11: You must play this card or discard it to trade hands',
						  '12', '12', '12', 'Safe', 'Safe', 'Safe', 'Sorry: Play this card to the discard pile, then draw a sorry card and play it', 'Sorry: Play this card to the discard pile, then draw a sorry card and play it',
						  'Sorry: Play this card to the discard pile, then draw a sorry card and play it', 'Sorry: Play this card to the discard pile, and then draw a sorry card and play it',
						  'Sorry: Play this card to the discard pile, then draw a sorry card and play it']
sorry_deck = ['Take a card of another player\'s set and discard it', 'Everyone but you must remove the last card from one of their sets', 'Take another player\'s set that is less than 9, and put the cards in your hand',
							   'Everyone gives you a card from their hand', 'Go home! Any one set of yours is now complete', 'Discard all 12\'s from all sets but yours', 'Look at another player\'s hand, if you are able, take one of those cards and play it',
							   'Look at another player\'s hand, if you are able, take one of those cards and play it', 'Draw 2 cards, if you are able play 1 of them and discard the other. Otherwise discard both', 'Draw 2 cards, if you are able play 1 of them and discard the other. Otherwise discard both',
							   'If you are able, take the last card from another player\'s set and add it to one of yours', 'If you are able, take the last card from another player\'s set and add it to one of yours']
# ALEX
class Hand(list):
	
	def playCard(self, card):
		Set().add(self.pop(self.index(card)))
		
	def add(self, card):
		self.append(card)
		
	def discard(self, cardIndex):
		DiscardDecks().cardDiscard(self.pop(cardIndex))
		
	def getCardIndex(self, card): # redundant, but may come in handy later.
		return self.index(card)
		
class Set(list):
	
	def add(self, card):
		self = map(int, self)
		total = 0
		for i in self:
			total += self.pop()
		
	def isComplete(self):
		self = map(int, self)
		total = 0
		for i in self:
			total += self.pop()
		if total > 15:
			return 'Over 15, not possible.'
		if total == 15:
			return True
		
	def getCardIndex(self, card):
		return self.index(card)
		
class Cards(object):

	def __init__(self, card_discard_deck=None, sorry_discard_deck=None):
		self.sorry_discard_deck = sorry_discard_deck
		self.card_discard_deck = card_discard_deck
		CardDeck().reshuffle()
		SorryDeck().reshuffle()
		
# JORDAN
class DiscardDecks(Cards):
		
	def cardDiscard(self, card):
		self.card_discard_deck.append(card)

	def sorryDiscard(self, card):
		self.sorry_discard_deck.append(card)
		
class CardDeck(Cards):
	
	def reshuffle(self): # shuffles the card deck
		random.shuffle(card_deck)
		
	def draw(self): # draws a card
		return card_deck.pop(random.randrange(len(card_deck)))

class SorryDeck(Cards):
	
	def reshuffle(self): # shuffles the sorry deck
		random.shuffle(sorry_deck)
		
	def draw(self):
		return sorry_deck.pop(random.randrange(len(sorry_deck)))