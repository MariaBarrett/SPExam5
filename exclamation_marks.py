#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import division
from collections import Counter
import pylab as pl

#tweets = ('tweets.txt')
fashion = ('tweets.txt')
#soccer = ('soccer.txt')

#split by double newline aka by every new tweet
fashion2 = open(fashion).read().split("\n\n")
#soccer2 = open(soccer).read().split("\n\n")

def averageexclamations(data):
    for tweet in data:
        counted = Counter(tweet)
        exclamationcount = counted['!']
        lenght = len(tweet)
        exclamationratio = exclamationcount / lenght
        average = exclamationratio / len(data)
        return average

fashionaverage = averageexclamations(fashion2)
averages = [fashionaverage]
classes = [fashion]

pl.clf()
pl.bar(pl.arange(len(averages)),averages)
pl.xticks(pl.arange(len(classes)),classes, rotation=80)
pl.show
#print ("result %s" % result)
