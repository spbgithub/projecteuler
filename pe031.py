'''Coin sums
Problem 31

In England the currency is made up of pound, , and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).

It is possible to make 2 in the following way:

    1x1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can 2 be made using any number of coins?
'''

coin_list = [1,2,5,10,20,50,100,200]

def change_counter(total_val, current_coin):
	if total_val == 0 or current_coin == 0:
		return 1
	elif current_coin == 0 and total_val > 0:
		return 0
	else:
		ret_val = 0
		cur_denom = coin_list[current_coin]

		for cur_coin in range(0, 1 + (total_val/cur_denom)):
			ret_val += change_counter(total_val - cur_coin * cur_denom, current_coin - 1)
		return ret_val

print(change_counter(200, 7))