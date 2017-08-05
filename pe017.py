'''
Number letter counts
Problem 17
Published on Friday, 17th May 2002, 06:00 pm; Solved by 92998; Difficulty rating: 5%
If the numbers5
 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

one_thousand = len("onethousand")
hundred = len("hundred")
len_and = len("and")
ones = []

ones = [0,len("one"),len("two"),len("three"),len("four"),len("five"),len("six"),len("seven"),len("eight"),len("nine")]
hundreds = [u + hundred for u in ones]

tens = [0,0,len("twenty"),len("thirty"),len("forty"),len("fifty"),len("sixty"),len("seventy"),len("eighty"),len("ninety"),len("ten"),len("eleven"),len("twelve"),len("thirteen"),len("fourteen"),len("fifteen"),len("sixteen"),len("seventeen"),len("eighteen"),len("nineteen")]

def num_to_word_length(num):
	total_length = 0
	if int(num / 1000) == 1:
		total_length = one_thousand
	else:
		num = num % 1000
		if int(num/100) > 0:
			total_length += hundreds[int(num / 100)]
			if num % 100 != 0:
				total_length += len_and

		num = num % 100

		if int(num / 10) == 0:
			total_length += ones[num % 10]
		elif int(num / 10) == 1:
			total_length += tens[num]
		else:
			total_length += tens[int(num / 10)] + ones[num % 10]
	return total_length

total = 0
for j in range(1, 1001):
	print(j, num_to_word_length(j))
	total += num_to_word_length(j)
print(total)