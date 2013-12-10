#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import division
from collections import Counter
import pylab as pl
import numpy as np

fashion = ('/Users/Maria/Documents/ITandcognition/Github/SPExam5/data/fashion.txt')
soccer = ('/Users/Maria/Documents/ITandcognition/Github/SPExam5/data/soccer.txt')

#fashion = ('/data/fashion.txt')
#soccer = ('/data/soccer.txt')

#split by double newline aka by every new tweet
fashion2 = open(fashion).read().split("\n\n")
soccer2 = open(soccer).read().split("\n\n")

def averageexclamations(data):
    for tweet in data:
  	averagelist =[]
     	counted = Counter(tweet)
        exclamationcount = counted['!']
       	lenght = len(tweet)
        exclamationratio = exclamationcount / lenght
        print exclamationratio
        average = exclamationratio / len(data)
     	averagelist.append(average)

fashionaverage = averageexclamations(fashion2)
socceraverage = averageexclamations(soccer2)

averages = [fashionaverage,socceraverage]
classes = [fashion,soccer]

print averages
