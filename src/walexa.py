from difflib import SequenceMatcher
import sys
import math
import struct
import time


def similar(a,b):
	return SequenceMatcher(None,a,b).ratio()



question_database={}


data=open("../public/data.csv","r")
lines=data.readlines()
for line in lines:
	q_and_a=line.split(",")
	question_database[q_and_a[0]]=q_and_a[1]

print(question_database)

question=open("question.txt","r").read()

print("User asked: "+str(question))

best_ratio=0
best_key="N/A"
for k in question_database.keys():
	if (similar(question,str(k))>best_ratio):
		best_ratio=similar(question,str(k))
		best_key=k
print("Highest ratio was"+str(best_ratio))
print("Your answer: "+str(question_database[best_key]))

f=open("answer.txt","w")
f.write(str(question_database[best_key]))
