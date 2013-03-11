#!/usr/bin/env python
# encoding: utf-8
"""
Problem1.py
Created for Project Euler
http://projecteuler.net/index.php?section=problems&id=1
Created by whimsy on 2010-04-26.
"""
"""
This problem finds the sum of all numbers that are multiples of 3 or 5 below 1000.
"""


def main():
	i=0
	j=0
	while i < 1000:
		if i%3==0 or i%5==0:
         j += i
		i += 1
	print j
	return 0


if __name__ == '__main__':
	main()

