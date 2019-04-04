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
tiers = [0, 1, 2, 3, 4, 5, 6, 7]
dpwr = {
	0: 0,
	1: 1,
	2: 2,
	3: 3,
	4: 5,
	5: 8,
	6: 13,
	7: 21
}
def calWeight(x):
	return x ** (x/2)

dweight = {
	0: 0,
	1: calWeight(dpwr[1]),
	2: calWeight(dpwr[2]),
	3: calWeight(dpwr[3]),
	4: calWeight(dpwr[4]),
	5: calWeight(dpwr[5]),
	6: calWeight(dpwr[6]),
	7: calWeight(dpwr[7])
}
weight = []
fl = []

def setFormula():
	global weight

	
	total = 0.0
	for x in range (len(tiers)):
		if dweight[x] != 0:
			total = total + 1.0/dweight[x]
	for x in range (len(tiers)):
		if dweight[x] != 0:
			weight.append(1.0/dweight[x]/total)
		else:
			weight.append(0.0)
	for x in range(len(weight)):
		print ("t" + str(x) + ":" + "{:.16f}".format(weight[x]*100) + "%")

def newDice():
	global dice
	power = 0
	dice = []
	for x in range(0,6):
		tier = numpy.random.choice(tiers, p=weight)
		power = power + dpwr[tier]
		dice.append('t' + str(tier))
	print ("Power " + str(power))


def permutate(l, tp, p, d, c, s, ttp, r):
	tp = tp + dpwr[p]
	if d == s+1:
		if tp in count:
			count[tp] += 1
		else:
			count[tp] = 1
		if ttp-r <= tp <= ttp:
			fl.append(copy.copy(c))
	else:
		for x in l:
			if x >= p:
			#if True:
				c.append(x)
				permutate(l,tp,x,d+1,c,s,ttp, r)
				c.remove(x)
	
def printDice():
	print (dice)

#def upgrade(s, l, i, st):

def main():
	global fl
	setFormula()
	while True:
		s = input().strip()
		if (s == 'q'):
			sys.exit(0)
		elif (s == 'd'):
			newDice()
			printDice()
		elif (s.startswith('p')):
			pms = s.split(' ')
			d = int (pms[1])
			p = int (pms[2])
			if len(pms) < 4:
				r = 5
			else:
				r = int(pms[3])
			permutate([1,2,3,4,5,6,7], 0, 0, 1, [], d, p, r)
			p = []
			for y in fl:
				total = 1.0
				for x in y:
					if dweight[x] != 0:
						total = total * 1.0/dweight[x]
				p.append(total)
			t = 0.0
			for x in p:
				t = t + x
			p1 = []
			for x in range(len(fl)):
				fl[x] = [(p[x]/t)*100] + (fl[x])
				#p1.append(x/t)
			fl.sort()
			for x in range(len(fl)):
				#print(str(fl[x]) + " " + )
				perc = fl[x].pop(0)
				print(str(fl[x]) + " " + "{:.6f}".format(perc) + "%")
			fl = []
			#for x in count.keys():
			#	print str(x) + ":" + str(count[x])

if __name__ == '__main__':
	main() 
