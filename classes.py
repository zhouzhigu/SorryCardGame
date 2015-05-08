
import random

computerPlayerNames = ["Bob","Mary"]

class Card(object):

	def __init__(self,value,instructions):
		self.setValue(value)
		self.setInstructions(instructions)

	def getValue(self):
		return self._value

	def setValue(self, value):
		self._value = value

	def getInstructions(self):
		return self._instructions

	def setInstructions(self, instructions):
		self._instructions = instructions

class Deck(object):

	def __init__(self,sorry=False):
		self._deck = []
		self._discard = []
		if sorry:
			self.addSorryCards()
		else:
			self.addPlayingCards()
		self.shuffle()

	def draw(self):
		return self._deck.pop()

	def shuffle(self):
		pass

	def discard(self,card):
		self._discard.append(card)

	def isEmpty(self):
		return len(self._deck) == 0

	def addPlayingCards(self):
		pass

	def addSorryCards(self):
		pass

class Set(object):

	def __init__(self):
		# Wes
		self._set = [0]
		self._complete = False

	def addCardToSet(self, card):
		# if set is complete, set it complete
		pass

	def removeCardFromSet(self,index=False):
		pass

	def isComplete(self):
		return self._complete

	def isSafe(self):
		pass

	def isEmpty(self):
		pass

	def testCard(self,card):
		if sum(self._set) + card < 16:
			return True
		else:
			return False

	def count(self):
		pass

class Hand(object):

	def __init__(self):
		# Wes
		self._hand = []

	def addCardToHand(self, card):
		pass

	def removeCardFromHand(self, index):
		pass

	def count(self):
		pass

class Player(object):

	def __init__(self, name, age):
		self.setName(name)
		self.setAge(age)

	def getName(self):
		return self._name

	def setName(self, name):
		self._name = name

	def getAge(self):
		return self._age

	def setAge(self, age):
		self._age = age

	def choosePlay(self):
		# return the card the player wants to play
		# must be legal to play
		pass

def CompPlayer(Player):

	def __init__(self):
		random.shuffle(computerPlayerNames)
		self.setName(computerPlayerNames.pop())
		self.setAge(random.randint(18,99))

	def choosePlay(self):
		# return the card the computer wants to play
		pass

class SorryGame(object):

	def __init__(self):
		self.currentPlayer = None
		self.playingDeck = Deck()
		self.sorryDeck = Deck("sorry cards")
		self._players = []
		self._winner = ''

	def addPlayer(self, player):
		pass

	def orderForPlay(self):
		pass

	def removeTwelves(self, exempt):
		for this_player in self._players:
			if this_player != exempt:
				twelvecount = 0
				for this_set in this_player.getSets():
					if 12 in this_set:
						this_set.remove(12)
						twelvecount += 1
				for len(twelvecount):
					Decks().discard(12)

	def playPlayingCard(self, card):
		# play the card
		# if it's a two, return True
		# if not, return False
		pass

	def playSorryCard(self):
		pass

	def nextPlayer(self):
		# return the next player

	def printResults(self):
		pass

	def gameOver(self):
		self.winner = False
		for this_player in self._players:
			if self.winner:
				return True
			num = 0
			for this_set in this_player.getSets():
				if this_set.isComplete() == True:
					num += 1
			if len(self._players) == 2 and num == 4:
				self._winner = this_player
			if len(self._players) == 3 and num == 3:
				self._winner = this_player
			if len(self._players) == 4 and num == 2:
				self._winner = this_player
		return False

	def move(self):
		pass
