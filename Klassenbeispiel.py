#Dies soll ein Beispiel für eine Klasse sein in Python

class make():
	def __init__ (self,color,length,height):
		color = self.color
		length = self.length
		height = self.height
	def car(color,length,height):
		print ("""The color is %s,the length is %s,The length is %s""" % (color,length,height))

# make.car("red","2.5","3")   Beispielausführung des Programms

class do(make):
    pass

# Beispiel von Klassenverebung in Python
# do.car("red","2.5","3")   Die Methode von der Klasse make wird vererbt

# Alpay Yildirim 06.08.2014   Python 3.4.1
