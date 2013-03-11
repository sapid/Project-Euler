#!/usr/bin/env python
# encoding: utf-8
"""
problem6.py

Created by whimsy on 2010-05-24.

This program finds the difference between the sum of the squares
 of the first one hundred natural numbers and the square of the sum.
"""


def main():
	sumsquare = 0
	squaresum = 0
	for a in range(0,101):
		sumsquare += a**2
		squaresum += a
   squaresum **= 2
	print squaresum - sumsquare
	return 0

if __name__ == '__main__':
	main()

