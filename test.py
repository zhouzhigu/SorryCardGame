import classes

class test(object):

	def __init__(self):
		self.p1 = classes.Hand()
		self.p2 = classes.Hand()
		
	def drawing(self):
		c1 = classes.CardDeck().draw()
		c2 = classes.CardDeck().draw()
		self.p1.add(c1)
		self.p2.add(c2)
		
	def printit(self):
		print self.p1
		print self.p2
		
test().drawing()
test().printit()