import sys
import os
import string
import re
import time
import math
import random

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

def printCard (cards):
	rValue = []
	for i in xrange(0,len(cards[0])):
		rValue.append(cards[0][i] + cards[1][i] + cards[2][i] + cards[3][i])
	for row in rValue:
		print ''.join(row)

def getSuit(c):
	if c == 'h':
		return [[' ', '_' , ' ' , ' ', '_', ' '],\
			    ['(', ' ' , '\\', '/', ' ', ')'],\
			    [' ', '\\', ' ' , ' ', '/', ' '],\
				[' ', ' ' , '\\', '/', ' ', ' ']]
	elif c == 'c':
		return [[' ', ' ' , '_', '_', ' ', ' '],\
			    [' ', '(' , ' ', ' ', ')', ' '],\
			    ['(', '_' , 'x', 'x', '_', ')'],\
				[' ', ' ' , ')', '(', ' ', ' ']]
	elif c == 'd':
		return [[' ', ' ' , '/' , '\\', ' ' , ' '],\
			    [' ', '/' , ' ' , ' ' , '\\', ' '],\
			    [' ', '\\', ' ' , ' ' , '/' , ' '],\
				[' ', ' ' , '\\', '/' , ' ' , ' ']]
	elif c == 's':
		return [[' ', ' ' , '/' , '\\', ' ' , ' '],\
			    [' ', '/' , ' ' , ' ' , '\\', ' '],\
			    ['(', '_' , ')' , '(' , '_', ')'],\
				[' ', ' ' , '/' , '\\' , ' ' , ' ']]

def getCard(l, n):
	if n == '11':
		n = 'J'
	elif n == '12':
		n = 'Q'
	elif n == '13':
		n = 'K'
	card = []
	card.append(['.','-','-','-','-','-','-','-','-','.'])
	if n == '10':
		card.append(['|', n ,' ',' ',' ',' ', n ,'|'])
	else:
		card.append(['|', n ,' ',' ',' ',' ',' ',' ', n ,'|'])
	for i in xrange(0,4):
		k = ['|',' ']
		for item in l[i]:
			k.append(item)
		k.append(' ')
		k.append('|')
		card.append(k)
	if n == '10':
		card.append(['|', n ,' ',' ',' ',' ', n ,'|'])
	else:
		card.append(['|', n ,' ',' ',' ',' ',' ',' ', n ,'|'])
	card.append(['.','-','-','-','-','-','-','-','-','.'])

	return card

def getDeck():
	return deck

if __name__ == '__main__':
	main() 