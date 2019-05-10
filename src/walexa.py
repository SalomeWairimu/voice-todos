from difflib import SequenceMatcher
import sys
import math
import struct
import time
import csv


class obj:
	def __init__(self, name):
		self.name = name
		self.who = None
		self.where = None 
		self.what = None 
		self.why = None 
		self.when = None 
		self.whispers = None 

	def get_ans(self, qst):
		qst = qst.lower()
		ans = ""
		if "who" in qst:
			ans = self.who
		elif "where" in qst:
			ans = self.where
		elif "what" in qst:
			ans = self.what
		elif "why" in qst:
			ans = self.why
		elif "when" in qst:
			ans= self.when
		else:
			ans = self.whispers
		return ans

objects = []
def initialize_everything():
	catobj = obj(name='the cat')
	catobj.who='Hyun Jung Jun  an art student at Northwestern University'
	catobj.what = "The cat is a flashe  linen  thread piece. Flashe is a vinyl-based  which can be used to create paintings on various mediums  such as linen and thread."
	catobj.where = 'The cat was created in Evanston  IL'
	catobj.why = 'For a thesis project'
	catobj.when = 'This was created in 2019'
	cruxobj = obj(name = 'the crucifixion')
	cruxobj.who= 'Naddo Ceccarelli'
	cruxobj.what = 'The crucifixion is a Tempera and gold on panel  gold leaf is gilded onto the wood panel before inscription and detailing'
	cruxobj.where = 'It was created in Siena Ital'
	cruxobj.why = 'The crucfixion is a depiction of Christs death  used in many Churches. These panel works were typically used in reliquaries'
	cruxobj.when = 'The crucifixion was created in the 14th century  circa 1350-1359'
	objects.append(catobj)
	objects.append(cruxobj)
		


def create_answer():
	question=open("question.txt","r").read()
	answ = "I don't understand"
	for elem in objects:
		if elem.name in question:
			print(elem.name)
			answ = elem.get_ans(question)
	f=open("answer.txt","w")
	f.write(str(answ))


initialize_everything()
create_answer()