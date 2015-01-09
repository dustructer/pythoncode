import sys
import os
import string
import re
import time
import math
import random

def draw():
	names = ["Michael Anthony Quan", "Yao Xiao", "David ChengWei Zhu", "Nicholas Lo", "Jerry Shen"]
	return random.choice(names)

def main():
	values = {"Michael Anthony Quan" : 0, "Yao Xiao": 0, "David ChengWei Zhu": 0, "Nicholas Lo": 0, "Jerry Shen": 0}
	for x in xrange(10):
		temp = draw()
		values[temp] = values[temp] + 1
	print values

if __name__ == '__main__':
	main()

9231
19500