from difflib import SequenceMatcher
import sys
import math
import struct
import time


def similar(a,b):
	return SequenceMatcher(None,a,b).ratio()



question_database={}

qst_audioID = {}

def populate_Id_dict():
	qst_audioID["biconical bead"] = ["1.mp3"]

def populate_qst_database():
	data=open("data.csv","r")
	lines=data.readlines()
	for line in lines:
		q_and_a=line.split(",")
		question_database[q_and_a[0]]=q_and_a[1]


def create_answer():
	question=open("question.txt","r").read()
	best_ratio=0
	best_key="N/A"
	for k in question_database.keys():
		if (similar(question,str(k))>best_ratio):
			best_ratio=similar(question,str(k))
			best_key=k
	if "Custom" in question_database[best_key].strip():
		answ = qst_audioID[best_key]
	else:
		answ = question_database[best_key]
	f=open("answer.txt","w")
	f.write(str(answ))


populate_Id_dict()
populate_qst_database()
create_answer()