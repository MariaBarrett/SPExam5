
#### Opening and closing data files! ####

f1 = open("data/untagged","r") #only read
f2 = open("data/tagged","r+") #read and write

print f2.read()

for line in f1:
	print "-" * 50
	print "Please annotate the following tweet token by token"
	print line

	"Guangliangs code goes here"
	f2.write(line)

	for word in line:
		print word
		tag = raw_input("Enter the POS-tag: ")
		if tag not in allowed:
			"reject!"


print f2.read()

allowed = ['ADV','VERB','NOUN','ADP','PRON','DET','.','PRT','NUM','X','CONJ','ADJ']

f1.close() #Remember to close whenever you're done with the file!
f2.close() #Same same