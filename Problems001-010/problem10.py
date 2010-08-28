#!/usr/bin/env python
# encoding: utf-8
"""
problem10.py

Created by yt on 2010-05-25.
Copyright (c) 2010 Will Crawford. All rights reserved.
"""

import sys
import os


def main():
	primes = [2, 3, 5, 7, 11, 13]
	i = 16
	while i < 2000001:
		i += 1
		for prime in primes:
			if i % prime == 0: 
				break
		else:
			primes.append(i)
	sum = 0
	for prime in primes:
		sum += prime
	print "Sum: " + str(sum)
	print "Number of primes: " + str(len(primes))
	return 0

if __name__ == '__main__':
	main()

