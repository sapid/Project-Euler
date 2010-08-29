#!/usr/bin/env python
# encoding: utf-8
"""
problem10.py

Created by whimsy on 2010-05-25.
Copyright (c) 2010 Will Crawford. All rights reserved.

This program should find the sum of all primes that are smaller than 2,000,000. 
It currently uses Atkin's sieve.
"""

import sys
import os
from math import sqrt

# I tried using this implementation first. Theoretically, it works. It's very slow, though.
def sieveEratosthenes(limit):
	primes = [2, 3, 5, 7, 11, 13]
	i = 15
	while i < limit:
		i += 2
		print "Checking: " + str(i)
		for prime in primes:
			if i % prime == 0: 
				break
		else:
			primes.append(i)
	return primes
	
# From http://stackoverflow.com/questions/1023768/sieve-of-atkin-explanation
# I don't understand this, but WOW is it fast!
def sieveAtkins(end):
	if end < 2: return []
	
	# Skip even numbers.
	lng = ((end/2) - 1 + end % 2)
	
	# Create our array. Assume everything is prime.
	sieve = [True] * (lng + 1)
	
	# Only go up to sqrt(end)
	for i in range(int(sqrt(end)) >> 1):
		print "Checking: " + str(i)
		# Skip numbers that aren't marked prime.
		if not sieve[i]: continue
		# Unmark all multiples of i, starting at i**2
		for j in range( (i*(i+3) << 1) +3, lng, (i<<1) + 3):
			sieve[j] = False
	
	primes = [2]
	primes.extend([(i<<1) + 3 for i in range(lng) if sieve[i]])
	return primes
	
def main():
	primes = sieveAtkins(2000001)
	print "Done finding primes. Summing..."
	sum = 0
	for prime in primes:
		sum += prime
	print "Sum: " + str(sum)
	print "Number of primes: " + str(len(primes))
	return 0

if __name__ == '__main__':
	main()

