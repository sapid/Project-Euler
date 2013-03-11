#!/usr/bin/env python
# encoding: utf-8
"""
problem7.py

Created by whimsy on 2010-05-24.

This program finds the 10001st prime number.
"""


def main():
	# We'll skip the first six primes.
	# 2, 3, 5, 7, 11, 13
	primes = [2, 3, 5, 7, 11, 13]
	i = 16
	while len(primes) < 10001:
		i += 1
		for prime in primes:
			if i % prime == 0: 
				break
		else:
			primes.append(i)
	# Our array is now populated with 10001 primes. 
	# The last one is the one we want.
	print primes[-1:]
	return 0


if __name__ == '__main__':
	main()

