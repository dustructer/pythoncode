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
	return x ** (x/4)

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
curL = []
curdw = []
curLs = []


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

def newDice(curdw, curLs):
	cdice = []
	chosen = numpy.random.choice(curLs, p=curdw)
	for x in chosen.split(','):
		cdice.append(int(x))
	cdice.append(curdw[curLs.index(chosen)]*100)
	return (cdice)

def permutate(l, tp, p, d, c, s, ttp, r):
	if tp + dpwr[p] <= ttp:
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
	
def printDice(dice):
	print(str(dice[:-1]) + " P" + str(calcP(dice[:-1])) + "\t{:>10.3}%".format(dice[-1]) + "\tAVP " + "{:.3}".format(calcT(dice[:-1])))

def calcP(dice):
	power = 0
	for p in dice:
		power = power + dpwr[p]
	return power

def calcT(dice):
	total = calcP(dice)
	return total/len(dice)
#def upgrade(s, l, i, st):

def main():
	global fl
	dice = []
	setFormula()
	while True:
		s = input().strip()
		if (s == 'q'):
			sys.exit(0)
		elif (s.startswith('d')):
			dms = s.split(' ')
			if len(dms) < 2:
				t = 1
			else:
				t = int(dms[1])
			for x in range(t):
				nd = newDice(curdw, curLs)
				printDice(nd)
				dice.append(nd)
		elif (s == 'l'):
			for x in dice:
				printDice(dice)
		elif (s.startswith('r')):
			rms = s.split(' ')
			ttp = int(rms[1])
			raid = True
			count = 0
			curTP = 0
			while raid:
				nd = newDice(curdw, curLs)
				count += 1
				dp = calcP(nd[:-1])
				if (dp > curTP):
					curTP = dp
					curTD = copy.deepcopy(nd)
				if (dp >= ttp) or (count >= 100000):
					printDice(curTD)
					print("Total raids: " + str(count))
					raid = False
				
		elif (s.startswith('p')):
			curdw = []
			curLs = []
			pms = s.split(' ')
			if len(pms) > 1:
				start_time = time.time()
				d = int (pms[1])
				if len(pms) < 3:
					p = d*13
				else:
					p = int (pms[2])
				if len(pms) < 4:
					r = p
				else:
					r = int(pms[3])
				permutate([1,2,3,4,5,6], 0, 0, 1, [], d, p, r)
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
				curL = copy.deepcopy(fl)	
				for x in curL:
					curdw.append(x.pop(0)/100.0)
					curLs.append(','.join(str(a) for a in x))
				for x in range(len(fl)):
					#print(str(fl[x]) + " " + )
					perc = fl[x].pop(0)
					print(str(fl[x]) + " P" + str(calcP(fl[x])) + " \t{:.5}".format(perc) + "%")
				end_time = time.time()
				print ("Excution took: " + "{:.8f}".format(end_time - start_time) + "ms")
				fl = []
				#for x in count.keys():
				#	print str(x) + ":" + str(count[x])

if __name__ == '__main__':
	main() 
