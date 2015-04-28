import random
# Class template for the sorry game

class Card(object):

	def __init__(self):
		pass

class Set(list, Hand):

	def __init__(self):

	def add(self, card):
		pass
		
	def isComplete(self):
		pass
		
	def getCardKey(self, card):
		pass
		
	def removeCardFromSet(self, card):
		pass
		
class Hand(list, Player):

	def add(self, card):
		pass
		
	def discard(self, cardIndex):
		pass
	
	def getCardIndex(self, card):
		pass
		
	def playCard(self):
		pass
		
class Player(object):

	def __init__(self):
		pass
		
	def addPlayer(self, name, age):
		pass
		
	def orderToPlay(self):
		pass
		
class Cards(object):

	def __init__(self):
		pass
		
class Decks(cards):

	def __init__(self):
		pass
		
	def playingCardDraw(self):
		pass
		
	def sorryCardDraw(self):
		pass
