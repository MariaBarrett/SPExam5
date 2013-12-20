from __future__ import division
from nltk import *
import nltk
import numpy as np
ftrain = open('twitterdata/tagged.txt').read().split('\n\n')
ftest  = open('twitterdata/test.google').read().split('\n\n')

train_list = [i.split('\n') for i in ftrain]
test_list  = [i.split('\n') for i in ftest]

def preparedata(train_list):
  inner = []
  outer = []
  Data1  = []
  Data2  = []
  
  for x in range(len(train_list)):
    inner = [m.lower().split('\t') for m in train_list[x]]
    outer.append(inner)
  train_data = outer
  
  train_data.remove(train_data[-1])
  for row in train_data:
      for ele in row:
          Data1.append((ele[0],ele[1]))
      Data2.append(Data1)
      Data1 = []
  return Data2
  
def preparedata2(train_list):
  inner = []
  outer = []
  Data1 = []
  Data2 = []
  
  for x in range(len(train_list)):
    inner = [m.lower().split('\t') for m in train_list[x]]
    outer.append(inner)
  train_data = outer

  train_data.remove(train_data[-1])
  for row in train_data:
      for ele in row:
          Data1.append(ele[0])
      Data2.append(Data1)
      Data1 = []
  return Data2


      
print 'Prepared the data'
sents = preparedata(train_list)
test_tagged  = preparedata(test_list)
test = preparedata2(test_list)

tagger = TnT()

print 'Start to train'
tagger.train(sents)


print 'Start to test'
tagged_data=tagger.tagdata(test)

print 'Start to caculate the accurancy'
accurancy=0
amount=0
for num in range(len(tagged_data)):
    for n in range(len(tagged_data[num])):
      amount+=1
      if test_tagged[num][n][1] == tagged_data[num][n][1]:
          accurancy += 1


accurancy=float(accurancy/amount)
print 'the accurancy of tagger is',accurancy

