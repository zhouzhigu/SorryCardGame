from random import randint, shuffle

class Hand(list):

	def add(self, card):
		self.append(card)
		
	def discard(self, card):
		self.remove(card)
		
class Cards(object):

	def __init__(self, card_count, sorry_count, card_deck, sorry_deck):
		self.card_count = 41
		self.sorry_count = 12
		self.card_deck = ['1', '1', '1', '1', '2: Go again', '2: Go again', '2: Go again', '2: Go again', '3: Take a card from an opponents hand',
						  '3: Take a card from an opponents hand', '3: Take a card from an opponents hand', '4: You must discard a card to play this one',
						  '4: You must discard a card to play this one', '4: You must discard a card to play this one', '5', '5', '5', '7: Remove and discard the top card from an opponents deck',
						  '7: Remove and discard the top card from an opponents deck', '7: Remove and discard the top card from an opponents deck', '8', '8', '8', '10 or -1', '10 or -1', '10 or -1',
						  '11: You must play this card or discard it to trade hands', '11: You must play this card or discard it to trade hands', '11: You must play this card or discard it to trade hands',
						  '12', '12', '12', 'Safe', 'Safe', 'Safe', 'Sorry: Play this card to the discard pile, then draw a sorry card and play it', 'Sorry: Play this card to the discard pile, then draw a sorry card and play it',
						  'Sorry: Play this card to the discard pile, then draw a sorry card and play it', 'Sorry: Play this card to the discard pile, and then draw a sorry card and play it',
						  'Sorry: Play this card to the discard pile, then draw a sorry card and play it']
		self.sorry_deck = ['Take a card of another player\'s set and discard it', 'Everyone but you must remove the last card from one of their sets', 'Take another player\'s set that is less than 9, and put the cards in your hand',
							   'Everyone gives you a card from their hand', 'Go home! Any one set of yours is now complete', 'Discard all 12\'s from all sets but yours', 'Look at another player\'s hand, if you are able, take one of those cards and play it',
							   'Look at another player\'s hand, if you are able, take one of those cards and play it', 'Draw 2 cards, if you are able play 1 of them and discard the other. Otherwise discard both', 'Draw 2 cards, if you are able play 1 of them and discard the other. Otherwise discard both',
							   'If you are able, take the last card from another player\'s set and add it to one of yours', 'If you are able, take the last card from another player\'s set and add it to one of yours']
		shuffle(self.card_deck)
		shuffle(self.sorry_deck)
	
class Decks(Cards):
	
	def cardReshuffle(self):
		pass
		
	def sorryReshuffle(self):
		pass
		
	def cardDiscard(self):
		pass
		
	def sorryDiscard(self):
		pass
		
	def deal(self):
		pass