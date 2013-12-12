#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import division
import sys, glob
import collections
from collections import Counter
import numpy as np


tweets = ('tweets.txt')

#split by double newline aka by every new tweet
tweets2 = open(tweets).read().split("\n\n")

tweetlist = [i.split() for i in tweets2]




POS_list=['adv', 'noun', 'adp', 'prt', 'det', 'num', '.', 'pron', 'verb', 'x', 'conj', 'adj']

for tweet in tweetlist:
    print tweet  
    for word in tweet:
        pos=raw_input('please input pos for %s:\n' % word)


        while( pos not in POS_list):
            print 'Please input the POS that excists in adv, noun, adp, prt, det, num, ., pron, verb, x, conj, adj, thanks '
            pos=raw_input('please input pos for %s:\n' % word)


"""
def prepare_data(train_list):
#this function returns a list of list of the train data. It has the following structure:
#[[tweet1[word1, pos1],[word2, pos2]...]] [tweet2[word1, pos1]...]...]. 
#converts to lowercase
  inner = []
  outer = []

  for x in range(len(train_list)):
    inner = [m.lower().split('\t') for m in train_list[x]]
    outer.append(inner)
  train_data = outer
  return train_data


x = int(raw_input('Enter first value: '))
y = int(raw_input('Enter second value: '))
method = (raw_input('Plus or minus? Enter p or m: '))

if method == "p":
	result = x + y
if method == "m":
	result = x - y 

print ("result %s" % result)

#name = raw_input('Enter your name: ')
#print ("Hi %s, Let us be friends" % name)

"""