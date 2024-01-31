import pygame
import time
import os
import random

HEIGHT = 60
WIDTH = 100

MAP = [[random.randint(0,1) for i in range(WIDTH)] for j in range(HEIGHT)]

f = open('pattern.txt')

BUFFER = [[[random.randint(0,1) for i in range(WIDTH)] for j in range(HEIGHT)]]


# MAP[30][50] = 1
# MAP[30][54] = 1
# MAP[30][55] = 1
# MAP[30][56] = 1
# MAP[31][50] = 1
# MAP[31][51] = 1
# MAP[31][52] = 1
# MAP[31][55] = 1
# MAP[32][51] = 1

newMAP = [[random.randint(0,1) for i in range(WIDTH)] for j in range(HEIGHT)]
oldMAP = [[random.randint(0,1) for i in range(WIDTH)] for j in range(HEIGHT)]

def printMAP():
	for i in MAP:
		for j in i:
			if j == 0:
				j = ' '
			else:
				j = '0'
			print(j, end=' ')
		print()

def returnAdjecents(i,j):
	ADJ = 0
	for I in range(-1,2,1):
		for J in range(-1,2,1):
			if i+I < 0 or i+I == len(MAP) or j+J < 0 or j+J == len(MAP[i]):
				continue
			if I == 0 and J == 0:
				continue

			# if i == 2 and j == 6:
			# 	print(i+I,j+J)
			# 	print(MAP[i+I][j+J])
			# 	print()
			ADJ += MAP[i+I][j+J]
	# if i == 2 and j == 6:
	# 	print(ADJ)
	return ADJ

def checkRepeat(target):
	isSame = True
	for M in BUFFER:
		for i in range(len(M)):
			for j in range(len(M[i])):
				if M[i][j] != target[i][j]:
					isSame = False
		if isSame:
			return True

	return isSame


os.system('clear')
ITER = 0
while True:
	newMAP = [[j for j in i] for i in MAP]
	printMAP()
	for i in range(len(MAP)):
		for j in range(len(MAP[i])):
			N = returnAdjecents(i,j)
			if MAP[i][j] == 1:
				if N == 3 or N == 2:
					newMAP[i][j] = 1
				else:
					newMAP[i][j] = 0
			else:
				if N == 3:
					newMAP[i][j] = 1

	if oldMAP == newMAP:
		print(ITER)
		ITER = 0
		newMAP = [[random.randint(0,1) for i in range(WIDTH)] for j in range(HEIGHT)]

		time.sleep(1)

	# if random.randint(0,1):
	# 	newMAP[random.randint(0,HEIGHT-1)][random.randint(0,WIDTH-1)] = random.randint(0,1)


	ITER += 1
			
	oldMAP = [[j for j in i] for i in MAP]




	MAP = [[j for j in i] for i in newMAP]
	
	# A = checkRepeat(MAP)
	# if A:
	# 	exit()

	BUFFER.append([[j for j in i] for i in MAP])
	if len(BUFFER) > 5:
		BUFFER.pop(0)

	time.sleep(0)
	os.system('clear')
	
	












