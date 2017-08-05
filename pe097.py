# -*- coding: utf-8 -*-
"""
Problem 97
"""

modulus = 10000000000
exp = 7830457
coeff = 28433

def pow(base, exp, modulus):
	if exp == 0:
		return 1
	if exp == 1:
		return base
	retval = pow(base, exp//2, modulus)
	if exp % 2 == 0:
		return (retval * retval) % modulus
	else:
		return (((retval * retval) % modulus) * base) % modulus
		
print((coeff * pow(2, exp, modulus) + 1) % modulus)
