import sys
import os
import string
import re
import time
import math
import random
import numpy
import copy

count = {}
dice = []
tiers = [0, 1, 2, 3, 4, 5, 6]
dpwr = {
	0: 0,
	1: 1,
	2: 2,
	3: 3,
	4: 5,
	5: 8,
	6: 13
}
dweight = {
	0: dpwr[6],
	1: dpwr[1] ** 1,
	2: dpwr[2] ** 2,
	3: dpwr[3] ** 3,
	4: dpwr[4] ** 4,
	5: dpwr[5] ** 5,
	6: dpwr[6] ** 6
}
weight = []
fl = []

def setFormula():
	global weight

	
	total = 0.0
	for x in range (0,7):
		total = total + 1.0/dweight[x]
	for x in range (0,7):
		weight.append(1.0/dweight[x]/total)
	print weight

def newDice():
	global dice
	power = 0
	dice = []
	for x in range(0,6):
		tier = numpy.random.choice(tiers, p=weight)
		power = power + dpwr[tier]
		dice.append('t' + str(tier))
	print "Power " + str(power)


def permutate(l, tp, p, d, c, s):
	tp = tp + dpwr[p]
	if d == s+1:
		if tp in count:
			count[tp] += 1
		else:
			count[tp] = 1
		if tp == 10:
			fl.append(copy.copy(c))
	else:
		for x in l:
			if x >= p:
				c.append(x)
				permutate(l,tp,x,d+1,c,s)
				c.remove(x)
	
def printDice():
	print dice

#def upgrade(s, l, i, st):

def main():
	setFormula()
	while True:
		s = raw_input().strip()
		if (s == 'q'):
			sys.exit(0)
		elif (s == 'd'):
			newDice()
			printDice()
		elif (s == 'p'):
			permutate(tiers, 0, 0, 1, [], 6)
			p = []
			for y in fl:
				total = 1.0
				for x in y:
					total = total * 1.0/dweight[x]
				p.append(total)
			t = 0.0
			for x in p:
				t = t + x
			p1 = []
			for x in p:
				p1.append(x/t)
			for x in range(len(fl)):
				print str(fl[x]) + " " + "{:.6f}".format(p1[x]*100) + "%"
			#for x in count.keys():
			#	print str(x) + ":" + str(count[x])

if __name__ == '__main__':
	main() 
