'''Poker hands (Problem 54)'''
import string

cards_in_order = "23456789TJQKA"

def hand_score(hand):
	if is_straight(hand) and is_flush(hand):
		if is_royal(hand):
			hscore = 90000 + hand[0][0]
		else:
			hscore = 80000 + hand[0][0]
	elif is_four_kind(hand):
		hscore = 70000 + hand[1][0]
	elif is_full_house(hand):
		hscore = 60000
		if hand[0][0] == hand[2][0]:
			hscore += 100 * hand[1][0] + hand[3][0]
		else:
			hscore += 100 * hand[3][0] + hand[1][0]
	elif is_flush(hand):
		hscore = 50000
	elif is_straight(hand):
		hscore = 40000 + hand[0][0]
	elif is_three_kind(hand):
		hscore = 30000 + hand[2][0]
	elif is_two_pair(hand):
		hscore = 20000 + 100 * hand[1][0] + hand[3][0]
	elif is_one_pair(hand):
		hscore = 10000
		if hand[0][0] == hand[1][0]:
			hscore += hand[0][0]
		elif hand[1][0] == hand[2][0]:
			hscore += hand[1][0]
		elif hand[2][0] == hand[3][0]:
			hscore += hand[2][0]
		else:
			hscore += hand[3][0]
	else:
		hscore = 0
	return 10**10 * hscore + sum([10**(8 - 2*j) * value(hand[j]) for j in range(0,5)])

def suit(card):
	return card[1]

def face_to_val(card):
	return string.find(cards_in_order, card[0])

def value(card):
	return card[0]

def is_straight(hand):
	for j in range(0,4):
		if hand[j][0] - hand[j+1][0] != 1:
			return False
	return True

def is_flush(hand):
	return len({hand[j][1] for j in range(0,5)}) == 1

def is_royal(hand):
	return is_straight(hand) and hand[0][0] == "A"

def is_four_kind(hand):
	return (value(hand[0]) == value(hand[3])) or (value(hand[1]) == value(hand[4]))

def is_full_house(hand):
	return (value(hand[0]) == value(hand[1]) and (value(hand[2]) == value(hand[4]))) or (value(hand[0]) == value(hand[2]) and (value(hand[3]) == value(hand[4])))

def is_three_kind(hand):
	return value(hand[0]) == value(hand[2]) or value(hand[1]) == value(hand[3]) or value(hand[2]) == value(hand[4])

def is_two_pair(hand):
	return (value(hand[0]) == value(hand[1]) and value(hand[2]) == value(hand[3])) or (value(hand[0]) == value(hand[1]) and value(hand[3]) == value(hand[4])) or (value(hand[1]) == value(hand[2]) and value(hand[3]) == value(hand[4]))

def is_one_pair(hand):
	return (value(hand[0]) == value(hand[1])) or (value(hand[1]) == value(hand[2])) or (value(hand[2]) == value(hand[3])) or (value(hand[3]) == value(hand[4]))


count = 0
with open("/home/sean/workspace/projecteuler/p054_poker.txt", "r") as f:
	for l in f:
		card = l.split()
		player_1 = sorted([(face_to_val(card[j]), card[j][1]) for j in range(0,5)])
		player_1.reverse()
		player_2 = sorted([(face_to_val(card[j]), card[j][1]) for j in range(5,10)])
		player_2.reverse()
		print(card[0:5])
		print(card[5:10])
		#print(player_1)
		#print(player_2)		
		print('{0:12d}'.format(hand_score(player_1)))
		print('{0:12d}'.format(hand_score(player_2)))
		if hand_score(player_1) == hand_score(player_2):
			print("fucked up somewhere")
		if hand_score(player_1) > hand_score(player_2):
			count += 1
		print("")
print(count)
