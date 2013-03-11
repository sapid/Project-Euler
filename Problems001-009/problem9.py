#!/usr/bin/env python
# encoding: utf-8
"""
problem9.py

Created by whimsy on 2010-05-24.

This program finds "a" and "b" for Problem 9 of Project Euler, but does not find C
although "a" and "b" must be correct by definition.

Magic formula by Mike Wilson; obtained by setting 
formulas against each other and isolating "C."
"""


def main():
	for b in range(0,1000):
		for a in range(0,b):
			# noinspection PyRedundantParentheses
         if (-10**6 == (2 * (a*b - a*10**3 - b*10**3) ) ):
				print a
				print b
				print " "
	return 0


if __name__ == '__main__':
	main()

