#!/usr/bin/env python
# encoding: utf-8
"""
problem10.py

Created by whimsy on 2010-05-25.

This program should find the sum of all primes that are smaller than 2,000,000. 
It currently uses Atkin's sieve.
"""

import sys
import os
from math import sqrt

# I rewrote the implementation of the sieve of erastothenes.
# It's a little more like Euler's Sieve now.
def sieveEratosthenes(limit):
	# Skip even numbers right off the bat.
	primes = range(3,limit+1,2)	
	for i in primes:
		print "Checking multiples of: " + str(i)
		j=2
		# Could this be sped up by making it a bit-field instead of a list? Search time would be O(1)...
		# ... but there would be no diminishing returns. len(primes) gets smaller and smaller as we go.
		while i * j < primes[-1]:
			if i*j%2 != 0: # This line is an attempt to optimize by not checking the list if i_j is even.
				if i*j in primes: # What's the run time for this search?
					primes.remove(i*j)
			j+=1
	primes.prepend(2) # We skipped this earlier, but 2 is prime!
	return primes

# From http://stackoverflow.com/questions/1023768/sieve-of-atkin-explanation
# I don't understand this, but WOW is it fast!
def sieveAtkins(end):
	if end < 2: return []
	
	# Skip even numbers.
	lng = ((end/2) - 1 + end % 2)
	
	# Create our array. Assume everything is prime.
	sieve = [True] * (lng + 1)
	
	# Only go up to sqrt(end) / 2
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
	primes = sieveEratosthenes(2000001)
	print "Done finding primes. Summing..."
	sum = 0
	for prime in primes:
		sum += prime
	print "Sum: " + str(sum)
	print "Number of primes: " + str(len(primes))
	return 0

if __name__ == '__main__':
	main()