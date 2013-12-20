from __future__ import division
import sys, glob
import collections
from collections import Counter
import numpy

#### Opening and closing data files! ####

#f1 = open("data/untagged","r") #only read
#f2 = open("data/tagged","r+") #read and write

f1 = open("data/untagged.txt","r") #only read
f2 = open("data/tagged.txt","a") #append to file

#split by double newline aka by every new tweet
tweets2 = f1.read().split("\n\n")

tweetlist = [i.split() for i in tweets2]


allowed = ['ADV','VERB','NOUN','ADP','PRON','DET','.','PRT','NUM','X','CONJ','ADJ','QUIT']
#print f2.read()



#--------------------------------------------------------------------------------------
#That annotation!
"""annotate()

"""
def annotate():
	for line in tweetlist:
		print "-" * 50
		print "Please annotate the following tweet token by token with the following tagset, \n use QUIT to quit."
		print allowed
		print line

		for word in line:
			tag = raw_input('please input pos for: %s ' % word)
			while tag not in allowed:
				tag = raw_input('please input pos for %s ' % word)
			else:
				if tag == "QUIT":
					userinput()
				else:
					f2.write(word)
					f2.write('\t')
					f2.write(tag)
			f2.write('\n')
		f2.write('\n')

	f1.close() #Remember to close whenever you're done with the file!
	f2.close() #Same same



#--------------------------------------------------------------------------------------
#TThat command line function of great win



def tag():
	"SOMETHING GOES HERE!?"


#--------------------------------------------------------------------------------------
#that interface

"""userinput()
This function is called at the beginning and takes a user input.
The input is then used as an ouput to call the commands(cmd) function.
"""
def userinput():
	print "="*60,"\n"
	print "Welcome to the best annotator tool in the world + more..\n"
	print "-"*45
	print "What do you want to do?\n"
	print "1. Annotate that shit"
	print "2. Tag that shit with the annotated shit"
	print "3. Quit that shit \n"
	print "-"*45
	uinput = raw_input("Please select a number: ")
	commands(uinput)



"""commands(cmd)
This function takes an integer as input.
Depending on the inputn, the function will either call the annotator function, the tagger, quit or even refer you back to the initial userinput.
When that function is done, it will call userinput() again.
"""
def commands(cmd):
	legal = ["1","2","3"]

	if cmd not in legal:
		print "No. Try again."
		userinput();

	elif cmd == "1":
		print "Tag the shit out of it"
		annotate()

	elif cmd == "2":
		tag()

	elif cmd == "3":
		print "Quit succesfully."
		raise SystemExit()

	userinput()



"""main()
Starts the programme by calling the userinput-function
"""
def main():
    print ">>> Welcome to the <best> annotator tool \n by Maria, Guangliang and Alexander \n Scientific Programming Exam 5 \n";
    userinput();


if __name__ =='__main__':
    main(); 
