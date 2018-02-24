#!/usr/bin/env python
import sys, pygame, copy, random
from square import Square
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

screen_size = (600,600)
dimensions = (rows,columns) = (4,4)
FPS = 60
black = (0,0,0)
#colors taken from https://yeun.github.io/open-color/
colors = [(134,142,150),(250,82,82),(230,73,128),(190,75,219),(121,80,242),(76,110,245),(34,138,230),(21,170,191),(18,184,134),(64,192,87),(130,201,30),(250,176,5),(253,126,20),(233,236,239),(255,236,153),(163,218,255)]
ideal_list = []
for i in range(columns):
	for j in range(rows):
		ideal_list.append(j*rows + i + 1)

def check_puzzle(puzzle):
	correct = True
	for i in range(rows * columns):
		if puzzle[i].label != str(ideal_list[i]):
			correct = False
			print("puzzle[i] is", puzzle[i].label, "but ideal_puzzle[i] = ", ideal_list[i])
	if correct:
		print("Hello")
	return correct

def calculate_xy(pos,puzzle):
	''' calculates which square is the target '''
	w = width / columns
	h = height / rows
	to_return = (int(pos[0]//w),int(pos[1]//h))
	return to_return

def print_square_colors(puzzle):
	for position in range(rows * columns):
		print(puzzle[position].color)

def print_square_prints(puzzle):
	for position in range(rows * columns):
		print(puzzle[position].label)

def find_square(puzzle):
	''' finds the black square '''
	for position in range(rows * columns):
		if puzzle[position].color == (0,0,0):
			return(position)
	return(0)

def move_space(puzzle, direction):
	''' moves black space up'''
	p = find_square(puzzle)
	blackSquare = puzzle[p]
	q = p
	if direction == "up":
		if (p % 4 != 0):
			print("UP")
			q = p - 1
		else:
			return puzzle
	elif direction == "down": #attempt to move the black square right
		if (p % 4 != 3):

			print("DOWN")
			q = p + 1
		else:

			return puzzle
	elif direction == "left":
		if (p > 3):
			print("LEFT")
			q = p - 4
		else:
			print(p)

			return puzzle
	elif direction == "right":
		if (p < 12):
			print("RIGHT")
			q = p + 4
		else:

			return puzzle
	puzzle[p] = puzzle[q]
	puzzle[q] = blackSquare
	puzzle[p].position, puzzle[q].position = puzzle[q].position, puzzle[p].position
	#puzzle[p].position = (puzzle[p].position[0] - 1, puzzle[p].position[1])
	#puzzle[p-1].position = (puzzle[p-1].position[0] + 1, puzzle[p-1].position[1])
	return puzzle


def main():
	print(ideal_list)
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	font = pygame.font.SysFont("arial",64)
	clock = pygame.time.Clock()
	possible_directions = ["up", "down", "left", "right"]


	puzzle = []
	(w,h) = (screen_size[0]/columns,screen_size[1]/rows)
	for i in range(rows):
		for j in range(columns):
			position = j*rows + i
			if position != 15:
				color = colors[position]
			elif position == 15:
				color = (0,0,0)
			puzzle.append(Square(i,j,str(position+1),w,h,color,font))
	increment = 0
	while increment < 5:
		increment += 1
		puzzle = move_space(puzzle, random.choice(possible_directions))





	while True:
		clock.tick(FPS)

		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					direction = "up"
				elif event.key == pygame.K_RIGHT:
					direction = "left"
				elif event.key == pygame.K_LEFT:
					direction = "right"
				elif event.key == pygame.K_UP:
					direction = "down"
				elif event.key == pygame.K_SPACE:
					print(check_puzzle(puzzle))
					direction = "down"
				puzzle = move_space(puzzle, direction)
				if check_puzzle(puzzle) == True:
					victory_text = "Wow!You won!gz!!"
					for i in range(rows * columns):
						puzzle[i].label = victory_text[i]
						if i < 4:
							color = (255, 255, 0)
						elif i < 8:
							color = (255, 0, 255)
						elif i < 12 :
							color = (0, 255, 255)
						elif i < 16:
							color = (255, 255, 255)
						puzzle[i].color = color




		for p in puzzle:
			p.draw_square(pygame.draw,screen)

		pygame.display.flip()

if __name__ == '__main__':
	main()
