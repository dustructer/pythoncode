def getCard(l, n):
	n = str(n)
	card = []
	card.append(['.','-','-','-','-','-','-','-','-','.'])
	card.append(['|', n ,' ',' ',' ',' ',' ',' ', n ,'|'])
	for i in xrange(0,4):
		k = ['|',' ']
		for item in l[i]:
			k.append(item)
		k.append(' ')
		k.append('|')
		card.append(k)
	card.append(['|', n ,' ',' ',' ',' ',' ',' ', n ,'|'])
	card.append(['.','-','-','-','-','-','-','-','-','.'])
	return card

def printCard (cards):
	rValue = []
	for i in xrange(0,len(cards[0])):
		rValue.append(cards[0][i] + cards[1][i] + cards[2][i] + cards[3][i])
	for row in rValue:
		print ''.join(row)


def main():
	cards = []
	cards.append(getCard(getSuit('h'), 3))
	cards.append(getCard(getSuit('c'), 3))
	cards.append(getCard(getSuit('d'), 3))
	cards.append(getCard(getSuit('s'), 3))
	printCard(cards)

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

if __name__ == '__main__':
	main()