import classes

class test(object):

	def __init__(self):
		self.p1 = classes.Hand()
		self.p2 = classes.Hand()	
		
	def drawing(self):
			i = 0
			while i < 6:
				c1 = classes.CardDeck().draw()
				c2 = classes.CardDeck().draw()
				self.p1.add(c1)
				self.p2.add(c2)
				i += 1
			print self.p1
			print self.p2

test().drawing()