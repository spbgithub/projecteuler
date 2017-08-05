with open("/home/sean/workspace/projecteuler/p089_roman.txt","r") as f:
	total = 0
	for l in f:
		if l.find("VIIII") > -1:
			total += 3
		elif l.find("IIII") > -1:
			total += 2

		if l.find("LXXXX") > -1:
			total += 3
		elif l.find("XXXX") > -1:
			total += 2

		if l.find("DCCCC") > -1:
			total += 3
		elif l.find("CCCC") > -1:
			total += 2

print(total)