import random

computerPlayerNames = [
"Bob","David","Steven","Luke","Chris","Molly","Lily","Rebecca",
"Clementine","Lee","John","Tom","Kenny","Alvin","Rick","Daryl",
"Marcus","Karen","Maya","Ed","Sharkie","Diane","Andy","Leon","Mary"
]

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

	def __str__(self):
		card_value = self.getValue()
		card_instructions = self.getInstructions()
		return '%s - %s' % (card_value, card_instructions)

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
		# Brendan
		# take all cards * if any * from self._discard
		# add to self._deck
		# and then shuffle self._deck
		pass

	def discard(self,card):
		self._discard.append(card)

	def isEmpty(self):
		return len(self._deck) == 0

	def addPlayingCards(self):
		for i in range(0,4):
			self._deck.append(Card(1, ""))
			self._deck.append(Card(2, "Go again"))
		for i in range(0,3):
			self._deck.append(Card(3, "Take a card from an opponent's hand"))
			self._deck.append(Card(4, "You must discard a card to play this one"))
			self._deck.append(Card(5, ""))
			self._deck.append(Card(7, "Remove and discard the top card from an opponent's set"))
			self._deck.append(Card(8, ""))
			self._deck.append(Card(10, "10 or -1"))
			self._deck.append(Card(11, "You must play this card or discard it to trade hands"))
			self._deck.append(Card(12, ""))
			self._deck.append(Card(0, "Safe: Cards cannot be removed from this set"))
		for i in range(0,6):
			self._deck.append(Card(99, "Sorry: Play this card to the discard pile. Then draw a sorry card and play it"))

	def addSorryCards(self):
		# Brendan
		pass

class Set(object):
	def __init__(self):
		self._set = []
		self._complete = False

	def addCardToSet(self, card):
		self._set.append(card)

	def removeCardFromSet(self,index):
		if not self.isSafe():
			return self._set.pop(index)
		return False

	def isComplete(self):
		return self._complete

	def isSafe(self):
		for thiscard in self._set:
			if thiscard.getValue()==0:
				return True
		return False

	def isEmpty(self):
		return len(self._set)==0

	def cardFits(self, card):
		if self.getValue() + card.getValue() < 16:
			return True
		return False

	def cardWins(self, card):
		if self.getValue() + card.getValue() == 15:
			return True
		return False

	def count(self):
		return len(self._set)

	def getValue(self):
		intset = []
		for this_card in self._set:
			intset.append(this_card.getValue())
		return sum(intset)

class Hand(object):
	def __init__(self):
		self._hand = []

	def addCardToHand(self, card):
		pass

	def removeCardFromHand(self, index):
		pass

	def count(self):
		return len(self.hand)

	def __str__(self):
		return "%s" % self._hand

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
		isReady == False
		while isReady == False:
			print self.currentPlayer.hand
			try:
				card = raw_input(int("choose a card to play "))
				discard = raw_input(int("choose card to discard "))
				setIndex = raw_input(int("set index "))
				noNumber = False
			except:
				noNumber = True
			if card.getValue() == 99:
				discard = card
				card = None
			if self.setIndex.cardFits(card) = True:
				isReady == True
		# I assume you want to do this after the loop breaks
		# so I unindented one level
		return card, discard, setIndex

	def getSets(self):
		return self._sets

	def __repr__(self):
		return "Player with Name %s and age %s" % (self.getName(), self.getAge())

	def __str__(self):
		return "%s" % self.getName()

class CompPlayer(Player):
	def __init__(self):
		random.shuffle(computerPlayerNames)
		self.setName(computerPlayerNames.pop())
		self.setAge(random.randint(18,102))

	def choosePlay(self):
		# Becky
		# return the card the computer wants to play
		# must be legal to play
		# you will return three objects
		# card the player wants to play (or None),
		# card the player wants to discard (or None),
		# the index of the set the player wants to add the card to
		# IF the player is "playing" the card that tells her to pick a sorry card,
		# return it as the discard
		setvalues = []
		for this_set in self.currentPlayer.getSets():
			setvalues.append(self.currentPlayer.getValue())
		cardvalues = []
		for card in self.currentPlayer.hand:
			cardvalues.append(card):
		for i, v in enumerate(setvalues):
			for card in self.hand
				if v + card.getValue() == 15:
					return i
				elif 99 in cadvalues:
					for j,card in enumerate(self.hand):
						if card.getValue() == 99:
							return i

class SorryGame(object):
	def __init__(self):
		self.currentPlayer = None
		self.playingDeck = Deck()
		self.sorryDeck = Deck("sorry cards")
		self._players = []
		self.winner = ''

	def getNumberOfPlayers(self):
		return len(self._players)

	def deal(self):
		# Chuck
		self.nextPlayer()
		if self.getNumberOfPlayers() == 2:
			numberOfSets = 4
		if self.getNumberOfPlayers() == 3:
			numberOfSets = 3
		if self.getNumberOfPlayers() == 4:
			numberOfSets = 2
		self.playingDeck.shuffle()
		self.sorryDeck.shuffle()
		for this_player in self._players:
			this_player._sets = []
			for i in range(numberOfSets):
				this_player._sets.append(Set())
			this_player.hand = Hand()
			for i in range(4):
				card = self.playingDeck.draw()
				this_player.hand.append(card)

	def orderForPlay(self):
		# Chuck
		self._players.sort(key=Player.getAge)

	def addPlayer(self, player):
		# Chuck
		self._players.append(player)

	def removeTwelves(self):
		for this_player in self._players:
			if this_player != self.currentPlayer:
				for this_set in this_player.getSets():
					for i, card in enumerate(this_set):
						thiscardvalue = i.getValue()
						if thiscardvalue == 0: # if the set has a safe card, shouldnt be here
							continue
						if thiscardvalue == 12:
							this_set.removeCardFromSet(i)
							self.playingDeck.discard(i)

	def playPlayingCard(self, card):
		# play the card
		# if it's a two, return True
		# if not, return False
		pass

	def playSorryCard(self):
		pass

	def nextPlayer(self):
		# Jordan
		# set self.currentPlayer to the next player
		self._players.append(self.currentPlayer)
		self.currentPlayer = self._player.pop(0)

	def printResults(self):
		print "Congratulations, %s ! You Won!" % self.winner

	def gameOver(self):
		# Alex
		for this_player in self._players:
			num = 0
			for this_set in this_player.getSets():
				if this_set.isComplete() == True:
					num += 1
			if len(self._players) == 2 and num == 4:
				self.winner = this_player
				return True
			if len(self._players) == 3 and num == 3:
				self.winner = this_player
				return True
			if len(self._players) == 4 and num == 2:
				self.winner = this_player
				return True
		return False

	def printPlayers(self):
		pass

	def move(self):
		theSets = self.currentPlayer.getSets()
		card, discard, setIndex = self.currentPlayer.choosePlay()
		try:
			cardValue = card.getValue()
		except:
			cardValue = None
		if isinstance(discard, Card):
			self.playingDeck.discard(card)
		if card is not None:
			if cardValue == 99: # the user would input the sorry card as the card, not discard - seems to make more sense to me this way, we can just discard it from here
				self.playingDeck.discard(card)
				self.playSorryCard()
			if cardValue in [-1, 1, 2, 4, 5, 8, 10, 12, 0]:
				theSets[setIndex].addCardToSet(card)
			if cardValue == 3:
				theSets[setIndex].addCardToSet(card)
				self.currentPlayer.Hand.addCardToHand(self.stealCardFromHand(card))
			if cardValue == 7:
				theSets[setIndex].addCardToSet(card)
				self.playingDeck.discard(self.stealCardFromSet(card))
			if cardValue == 11:
				theSets[setIndex].addCardToSet(card)
				self.tradeHands(self.currentPlayer)
			elif discardValue == 11:
				self.playingDeck.discard(card)
				self.tradeHands(self.currentPlayer) # same logic as the if statement above, just changes if its being discarded instead of being played
		if cardValue != 2:
			self.nextPlayer()