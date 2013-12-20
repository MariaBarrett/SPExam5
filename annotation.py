from __future__ import division
import collections
import subprocess

#### Opening and closing data files! ####

f1 = open("data/untagged.txt","r") #only read
f2 = open("data/tagged.txt","a") #append to file
f3 = open("data/tnttagged.txt","w")

taggedfile = ("data/tagged.txt")
lex  = "data/tagged.lex"
num = "data/tagged.123"

#split by double newline aka by every new tweet
tweets2 = f1.read().split("\n\n")

tweetlist = [i.split() for i in tweets2]


allowed = ['ADV','VERB','NOUN','ADP','PRON','DET','.','PRT','NUM','X','CONJ','ADJ','QUIT']
legal = ["1","2","3"]
#print f2.read()



#--------------------------------------------------------------------------------------
#That annotation!
"""annotate()
This function reads every line the file containing untagged tweets and splits byt space characters.
It presents the user for the entire tweets, then it presents one word at a time and expects the user to input a POS.
A while loop ensures that only valid input is accepted. Word, tab, tag and newline is written to a new file plus an extra newline after last word of a tweet.

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
#That command line function of great win

"""tag()
This function takes a userspecified input, derived from the raw_input, and calls the function tagging() with that input.

"""
def tag():
	print "\n What do you want to do? \n"
	print "-"*45
	print "1. Train the tagger"
	print "2. Tag train.google with the tagger"
	print "3. Return to main menu"
	print "-"*45

	utag = raw_input("Please select a number: ")
	tagging(utag)



"""tagging(cmd)
This function takes a string as its input and checks if it is the legal variable.
Depnding on that, it will either return to the tag() function, train the TnT tagger, run the TnT tagger on test.google or quit.
When done, it calls the tag menu.

"""
def tagging(cmd):

	if cmd not in legal:
		print "No. Try again."
		tag();

	elif cmd == "1":
		subprocess.call(["tnt-para","-i",taggedfile])
		subprocess.call(["mv","tagged.lex",lex])
		subprocess.call(["mv","tagged.123",num])
		"TnT training completed."
		tag()

	elif cmd == "2":
		print "Tagging with TnT."
		t = subprocess.Popen(["tnt",lex,num,"data/test.google"],stdout=subprocess.PIPE).communicate()[0]
		f3.write(t)

		print "\n"
		subprocess.call(["tnt-diff","data/test.google","data/tnttagged.txt"])

		tag()

	elif cmd == "3":
		userinput()



#--------------------------------------------------------------------------------------
#that interface - Much wow many amaze

"""userinput()
This function is called at the beginning and takes a user input.
The input is then used as an ouput to call the commands(cmd) function.
"""
def userinput():
	print "="*60,"\n"
	print "Welcome to the best annotator tool in the world + more..\n"
	print "-"*45
	print "What do you want to do?\n"
	print "1. Use the annotator tool"
	print "2. Use the fancy TnT-tagger"
	print "3. Quit \n"
	print "-"*45
	uinput = raw_input("Please select a number: ")
	commands(uinput)



"""commands(cmd)
This function takes an integer as input.
Depending on the inputn, the function will either call the annotator function, the tagger, quit or even refer you back to the initial userinput.
When that function is done, it will call userinput() again.
"""
def commands(cmd):

	if cmd not in legal:
		print "No. Try again."
		userinput();

	elif cmd == "1":
		annotate()

	elif cmd == "2":
		tag()

	elif cmd == "3":
		print "Quit succesfully."
		f3.close()
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
