'''
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Note: our convention for days will have Sunday=0, Monday=1, ..., Saturday=6

'''



days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year_correction(cur_month, cur_year):
	ret_val = 0
	if (cur_month != 1):
		return 0
	if ((cur_year % 4 == 0 and cur_year % 100 != 0) or (cur_year % 100 != 0 and cur_year % 400 == 0)):
		return 1
	return 0

current_day = 1
current_month = 0
current_year = 1900
total_sundays = 0

while (current_year < 2001):
	for d in days_in_month:
		current_day = (current_day + d + leap_year_correction(current_month, current_year)) % 7
		if (current_year >= 1901 and current_year <= 2000):
			if current_day == 0:
				total_sundays += 1
	current_year += 1
print(total_sundays)