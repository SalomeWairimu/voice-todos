

def create_answer():
	question=open("mylocation.txt","r").read()
	answ = "I don't understand"
	for row in question:
        if '1' in row:
            answ = "'You are in front of the cat painting. Created by Hyun Jung Jun"
        else:
            answ = 'this is the crucifixion. The crucifixion is a Tempera and gold on panel  gold leaf is gilded onto the wood panel before inscription and detailing'
	f=open("answer.txt","w")
	f.write(str(answ))

create_answer()