from random import randint, shuffle

# ALEX
class Hand(list):
	
	def printHand(self):
		pass
		
	def add(self, card):
		self.append(card)
		
	def discard(self, card):
		Cards().cardDiscard(self.pop(card))
		
class Cards(object):

	def __init__(self, card_count, sorry_count, card_deck, sorry_deck, sorry_discard_deck, card_discard_deck):
		self.card_count = 41
		self.sorry_count = 12
		self.card_deck = card_deck
		self.sorry_deck = sorry_deck
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
		self.sorry_discard_deck = _sorry_discard_deck
		self.card_discard_deck = _card_discard_deck
		shuffle(card_deck) # subject to change
		shuffle(sorry_deck) # subject to change
		
	def cardDiscard(self, card):
		_card_discard_deck.append(card)

	def sorryDiscard(self, card):
		_sorry_discard_deck.append(card)
		
# JORDAN		
class CardDeck(Cards):
	
	def reshuffle(self): # shuffles the card deck
		shuffle(card_deck)
		
	def draw(self): # draws a card
		c = card_deck.pop(random.choice())
		return c # returns the chosen card for the game logic to add to the players hand
		
class SorryDeck(Cards):
	
	def reshuffle(self): # shuffles the sorry deck
		shuffle(sorry_deck)
		
	def draw(self):
		c = sorry_deck.pop(random.choice())
		return c # returns the chosen card for the game logic to add to the players hand