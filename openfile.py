from __future__ import division
import sys, glob
import collections
from collections import Counter
import numpy

#### Opening and closing data files! ####

#f1 = open("data/untagged","r") #only read
#f2 = open("data/tagged","r+") #read and write

f1 = open("/Users/Maria/Documents/ITandcognition/Github/SPExam5/data/untagged.txt","r") #only read
f2 = open("/Users/Maria/Documents/ITandcognition/Github/SPExam5/data/tagged.txt","a") #append to file

#split by double newline aka by every new tweet
tweets2 = f1.read().split("\n\n")

tweetlist = [i.split() for i in tweets2]



allowed = ['ADV','VERB','NOUN','ADP','PRON','DET','.','PRT','NUM','X','CONJ','ADJ']
#print f2.read()

for line in tweetlist:
	print "-" * 50
	print "Please annotate the following tweet token by token"
	print line

	for word in line:
		tag = raw_input('please input pos for: %s ' % word)
		while tag not in allowed:
			tag = raw_input('please input pos for %s ' % word)
		else:
			f2.write(word)
			f2.write('\t')
			f2.write(tag)
		f2.write('\n')
	f2.write('\n')

f1.close() #Remember to close whenever you're done with the file!
f2.close() #Same same