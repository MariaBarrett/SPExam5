#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import division
from collections import Counter
import pylab as pl
import numpy as np


fashion = ('/data/fashion.txt')
soccer = ('/data/soccer.txt')

#split by double newline aka by every new tweet
fashion2 = open(fashion).read().split("\n\n")
soccer2 = open(soccer).read().split("\n\n")

print len(fashion2)
print len(soccer2)

def averageexclamations(data):
    averagelist =[]
    sum = 0
    for tweet in data[:-1]: #empty tweet
       	counted = Counter(tweet)
        exclamationcount = counted['!']
       	lenght = len(tweet)
        exclamationratio = exclamationcount / lenght
        average = exclamationratio / len(data)
        sum += average
    Average = sum/len(data) * 100
    return Average
   

fashionaverage = averageexclamations(fashion2)
socceraverage = averageexclamations(soccer2)

averages = [fashionaverage,socceraverage]
classes = [fashion,soccer]

print averages
