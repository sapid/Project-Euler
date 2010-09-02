#!/usr/bin/env python
# encoding: utf-8
"""
problem3.py

Created by whimsy on 2010-04-26.

isprime(n) by vegaseat from daniweb.com (http://www.daniweb.com/code/snippet216880.html)
This program is intended to...
Determine the largest prime factor of the number 600851475143.
"""

import sys
import os
import math

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def main():
	a = int(600851475143**.5)
	answer = 0
	while answer == 0 and a>=0:
		a=a-1
		if 600851475143%a==0 and isprime(a):
			answer = a
	print answer
	return 0

if __name__ == '__main__':
	main()

