import sys
import os
import string
import re
import time
import math
import random
from cards import getSuit, getCard

deck = []

def newDeck():
	global deck
	deck = []
	for x in xrange(1,14):
		for y in ['h','c','s','d']:
			deck.append(str(x) + ';' + str(y))

def shuffle():
	random.shuffle(deck)
	
def printDeck():
	print deck

def calculate(s, l, i, st):
	o = st
	if i > 3 :
		if s == 24:
			return st
		else:
			return '0'
	else:
		k = float(l[i])
		st = o + ' + ' + str(int(k))
		if (calculate(s+k, l, i +1, st) != '0'):
			return calculate(s+k, l, i +1, st)
		st = o + ' - ' + str(int(k))
		if (calculate(s-k, l, i +1, st) != '0'):
			return calculate(s-k, l, i +1, st)
		if len(o) != 1:
			st = '(' + o + ') * ' + str(int(k))
		else:
			st = o + ' * ' + str(int(k))
		if (calculate(s*k, l, i +1, st) != '0'):
			return calculate(s*k, l, i +1, st)
		if len(o) != 1:
			st = '(' + o + ') / ' + str(int(k))
		else:
			st = o + ' / ' + str(int(k))
		if (calculate(s/k, l, i +1, st) != '0'):
			return calculate(s/k, l, i +1, st)
		return '0'

def copy(l):
	lc = []
	for i in l:
		lc.append(i)
	return lc

def permutate(l,m,k):
	for a in l:
		k1 = copy(k)
		l1 = copy(l)
		k1.append(a)
		l1.remove(a)
		if len(l) == 1:
			m.append(k1)
		else:
			permutate(l1, m, k1)
		k1 = copy(k)
	return m

def printCard (cards):
	rValue = []
	for i in xrange(0,len(cards[0])):
		rValue.append(cards[0][i] + cards[1][i] + cards[2][i] + cards[3][i])
	for row in rValue:
		print ''.join(row)

def main():
	newDeck()
	shuffle()
	print 'Welcome to the 24 game!'
	print 'Type play to play a new round.'
	print 'Type help for a list of commands.'
	try:
		while True:
			l = []
			ls = []
			s = raw_input('Enter input: ').strip()
			if len(deck) < 4:
				newDeck()
				shuffle()
			if s in ['exit', 'q']:
				sys.exit(0)
			elif (s == 'play'):
				os.system('clear')
				for x in xrange(0,4):
					card = deck.pop(0).split(';')
					l.append(str(card[0]))
					ls.append(str(card[1]))
				cards = []
				for i in xrange(0,4):
					cards.append(getCard(getSuit(ls[i]), l[i]))
				printCard(cards)
				et = time.time()
				m = []
				k = []
				m = permutate(l,m,k)
				found = False
				for m1 in m:
					st = m1[0]
					if calculate(float(m1[0]), m1, 1, st) != '0':
						found = True
						break
				if not found:
					print 'no solution. play again'
				else:
					print 'Elapsed calculation time : ' + str(round((time.time()-et)*10000)/10) + ' ms'
					t = time.time()
					raw_input("Press enter to show sample solution")
					print 'it took you : ' + str(round((time.time()-t)*10)/10) + ' seconds!'
					print calculate(float(m1[0]), m1, 1, st)
			elif (s == 'new'):
				newDeck()
				os.system('clear')
				print 'A new ordered deck has been made.'
				print 'Enter \'shuffle\' to shuffle the deck.'
				print 'Enter \'play\' to play a new round.'
			elif (s == 'shuffle'):
				shuffle()
				print 'The deck has been shuffled.'
			elif (s == 'show'):
				printDeck()
			elif (s == 'help'):
				os.system('clear')
				print ('play - new round')
				print ('new - create new ordered deck')
				print ('shuffle - shuffle current deck')
				print ('show - show current deck')
				print ('exit - exit program')
			else:
				print 'Unrecognized Command'
				print 'Type help for command list'
	except Exception as e:
		print 'unexpected error. exiting'
		sys.exit(1)

if __name__ == '__main__':
	main() 
