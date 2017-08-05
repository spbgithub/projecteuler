from random import randrange
from collections import deque

class dice_roll:
	def __init__(self, n):
		self.die_sides = n
		self.last_two  = [[0,-1],[0,-1]]
		self.current_roll = [0,-1]

	#is a given roll a double
	def is_double(self, dpair):
		return dpair[0] == dpair[1]

	#do we have three doubles in a row?
	def is_three_doubles(self):
		if sum(self.last_two[0]) > 1 and sum(self.last_two[1]) > 1:
			if self.is_double(self.last_two[0]) and self.is_double(self.last_two[1]) and self.is_double(self.current_roll):
				return True
		return False

	#returns whether or not the three doubles condition is satisfied, along with the
	#value of the current roll
	def roll_dice(self):
		#if is_three_doubles() is already true, then we leave on this roll, so reinit
		#the previous roll values
		d1 = randrange(1, self.die_sides + 1)
		d2 = randrange(1, self.die_sides + 1)
		self.last_two = (self.last_two + [self.current_roll])[1:]
		self.current_roll = [d1, d2]
		return self.is_three_doubles(), sum(self.current_roll)

def randomize_cards(card_list):
	permuted_cards = deque()
	while len(card_list) > 0:
		n = randrange(0, len(card_list))
		permuted_cards.append(card_list[n])
		card_list.pop(n)
	return permuted_cards

GO_TO_JAIL = 30
JAIL       = 10
DIE_SIDES  = 6

squares = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

chance_cards_init    =  ['GO', 'JAIL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
commchest_cards_init =  ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'R', 'R', 'U', -3, 0, 0, 0, 0, 0, 0]

distribution = [0] * 40
ROUNDS = 500000
cur_sq = 0
dice = dice_roll(DIE_SIDES)
comm = randomize_cards(chance_cards_init)
ch   = randomize_cards(commchest_cards_init)

def find_next_specified(cur_loc, seeking):
	cur_loc = (cur_loc + 1) % 40
	while seeking not in squares[cur_loc]:
		cur_loc = (cur_loc + 1) % 40
	return cur_loc

def find_next_railroad(cur_loc):
	return find_next_specified('R')

def find_next_utility(cur_loc):
	return find_next_specified('U')

def next_square(current_square, roll_generator):
	dbls, roll = roll_generator.roll_dice()
	if dbls:
		return JAIL
	else:
		current_square = (current_square + roll) % 40
		if (current_square == GO_TO_JAIL): #go to jail squares
			return JAIL
		card = False
		if "CC" in squares[current_square]:
			card = comm[0]
			comm.rotate()

		elif "CH" in squares[current_square]:
			card = ch[0]
			ch.rotate()

		if type(card) is int:
			current_square = (current_square + card) % 40
		elif type(card) is str:
			current_square = find_next_specified(current_square, card)

		return current_square

distribution[cur_sq] += 1
for r in range(0, ROUNDS):
	cur_sq = next_square(cur_sq, dice)
	distribution[cur_sq] += 1

rankings = sorted([(float(distribution[j])/float(ROUNDS), j) for j in range(0, 40)])
rankings.reverse()
for j in range(0, 3):
	print(rankings[j])