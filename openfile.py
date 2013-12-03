
#### Opening and closing data files! ####

f1 = open("data/untagged","r") #only read
f2 = open("data/tagged","r+") #read and write

print f2.read()

for line in f1:
	print line
	"Guangliangs code goes here"
	f2.write(line)

print f2.read()

f1.close() #Remember to close whenever you're done with the file!
f2.close() #Same same