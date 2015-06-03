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

	def __repr__(self):
		card_value = self.getValue()
		card_instructions = self.getInstructions()
		return '%s - %s' % (card_value, card_instructions)

	__str__ = __repr__


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
		for this_card in self._discard:
			self._deck.append(this_card)
		for i in range(7):
			random.shuffle(self._deck)

	def discard(self,card):
		self._discard.append(card)

	def isEmpty(self):
		return len(self._deck) == 0

	def addPlayingCards(self):
		for i in range(4):
			self._deck.append(Card(1, ""))
			self._deck.append(Card(2, "Go again"))
		for i in range(3):
			self._deck.append(Card(3, "Take a card from an opponent's hand"))
			self._deck.append(Card(4, "You must discard a card to play this one"))
			self._deck.append(Card(5, ""))
			self._deck.append(Card(7, "Remove and discard the top card from an opponent's set"))
			self._deck.append(Card(8, ""))
			self._deck.append(Card(10, "10 or -1"))
			self._deck.append(Card(11, "You must play this card or discard it to trade hands"))
			self._deck.append(Card(12, ""))
			self._deck.append(Card(0, "Safe: Cards cannot be removed from this set"))
		for i in range(6):
			self._deck.append(Card(99, "Sorry: Play this card to the discard pile. Then draw a sorry card and play it"))

	def addSorryCards(self):
		for i in range(2):
			self._deck.append(Card(1, "Draw 2 cards. If you are able, play one of them and discard the other. Otherwise discard both"))
			self._deck.append(Card(2, "Look at another player's hand. If you are able, take one of those cards and play it."))
			self._deck.append(Card(3, "If you are able, take the last card from another player's set and add it to one of yours"))
		self._deck.append(Card(4, "Take the top card of another player's set and discard it"))
		self._deck.append(Card(5, "Everyone but you must remove the last acrd from one of their sets."))
		self._deck.append(Card(6, "Take another player's set that is less than 9, and put the cards in your hand."))
		self._deck.append(Card(7, "Everyone gives you a card from their hand"))
		self._deck.append(Card(8, "Discard all 12's from all sets but yours"))
		self._deck.append(Card(9, "Go Home! Any one set of yours is now complete."))


class Set(object):
	def __init__(self):
		self._set = []
		self._complete = False

	def addCardToSet(self, card):
		if not self.isSafe():
			self._set.append(index)

	def removeCardFromSet(self,index):
		if not self.isSafe():
			return self._set.pop(index)

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
		return (self.getValue() + card.getValue() < 16) or False

	def cardWins(self, card):
		return (self.getValue() + card.getValue() == 15) or False

	def count(self):
		return len(self._set)

	def getValue(self):
		intset = []
		for this_card in self._set:
			intset.append(this_card.getValue())
		return sum(intset)

	def __repr__(self):
		# Return a printable version of the set
		pass

	__str__ = __repr__

class Hand(object):
	def __init__(self):
		self._hand = []

	def addCardToHand(self, card):
		self._hand.append(card)

	def removeCardFromHand(self, index):
		return self._hand.pop(index)

	def count(self):
		return len(self._hand)

	def __repr__(self):
		# Return a printable version of the hand
		pass

	__str__ = __repr__


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
		# Matt
		# return the card the player wants to play
		# must be legal to play
		# you will return three objects
		# card the player wants to play (or None),
		# card the player wants to discard (or None),
		# the index of the set the player wants to add the card to
		# IF the player is "playing" the card that tells her to pick a sorry card,
		# return it as the discard
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
			if self.setIndex.cardFits(card) == True:
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
			cardvalues.append(card)
		for i, v in enumerate(setvalues):
			for card in self.hand:
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
		self.winner = None

	def getNumberOfPlayers(self):
		return len(self._players)

	def deal(self):
		# Chuck
		self.nextPlayer()
		numPlayers = self.getNumberOfPlayers()
		if numPlayers == 2:
			numberOfSets = 4
		if numPlayers == 3:
			numberOfSets = 3
		if numPlayers == 4:
			numberOfSets = 2
		self.playingDeck.shuffle()
		self.sorryDeck.shuffle()
		for this_player in self._players:
			print this_player
			this_player._sets = []
			for i in range(numberOfSets):
				this_player._sets.append(Set())
			this_player.hand = Hand()
			for i in range(4):
				card = self.playingDeck.draw()
				this_player.hand.addCardToHand(card)

	def orderForPlay(self):
		self._players.sort(key=Player.getAge)

	def addPlayer(self, player):
		self._players.append(player)

	def drawTwo(self):
		# draw 2 cards, if you are able, play one of them and discard the other. otherwise discard both
		pass

	def lookTakeAndPlay(self):
		# look at another player's hand. if you are able, take one of those cards and play it
		pass

	def takeLastCard(self):
		# if you are able, take the last card from another player's set and add it to one of yours
		pass

	def takeTopCard(self):
		# take the top card of another player's set and discard it
		pass

	def removeLastCard(self):
		# everyone but you must remove the last card from one of their sets
		pass

	def takeSet(self):
		# take another player's set, that is less than 9, and put the cards in your hand
		pass

	def opponentsGiveACard(self):
		# everyone gives you a card from their hand
		pass

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

	def completeSet(self):
		# go home! any one set of yours is now complete
		pass

	def playSorryCard(self):
		cardValue = card.getValue()
		if cardValue == 1:
			self.currentPlayer.drawTwo()
		elif cardValue == 2:
			self.currentPlayer.lookTakeAndPlay()
		elif cardValue == 3:
			self.currentPlayer.takeLastCard()
		elif cardValue == 4:
			self.currentPlayer.takeTopCard()
		elif cardValue == 5:
			self.currentPlayer.removeLastCard()
		elif cardValue == 6:
			self.currentPlayer.takeSet()
		elif cardValue == 7:
			self.currentPlayer.opponentsGiveACard()
		elif cardValue == 8:
			self.removeTwelves()
		elif cardValue == 9:
			self.currentPlayer.completeSet()

	def nextPlayer(self):
		# Jordan
		# set self.currentPlayer to the next player
		pass
		#self._players.append(self.currentPlayer)
		#self.currentPlayer = self._players.pop(0)

	def printResults(self):
		print "Congratulations, %s ! You Won!" % self.winner

	def gameOver(self):
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
			# the user would input the sorry card as the card, not discard
			if cardValue == 99:
				self.playingDeck.discard(card)
				self.playSorryCard()
			else:
				theSets[setIndex].addCardToSet(card)
		if cardValue != 2:
			self.nextPlayer()
