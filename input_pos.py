from __future__ import division
import sys, glob
import collections
from collections import Counter
import numpy

POS_list=['adv', 'noun', 'adp', 'prt', 'det', 'num', '.', 'pron', 'verb', 'x', 'conj', 'adj']

pos=raw_input('please input the pos:\n')


while( pos not in POS_list):
    print 'Please input the POS that excists in adv, noun, adp, prt, det, num, ., pron, verb, x, conj, adj, thanks '
    pos=raw_input('please input the part of speech\n')