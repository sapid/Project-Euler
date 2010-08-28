#!/usr/bin/env python
# encoding: utf-8
"""
problem4.py

Created by whimsy on 2010-05-10.
Copyright (c) 2010 Will Crawford. All rights reserved.
This program finds the largest palindrome made from the product of two 3-digit numbers.
"""

import sys
import os


def main():
	largest = 0
	for b in range(999,100,-1):
		for a in range(999,100,-1):
			if ( (str(a*b) == str(a*b)[::-1]) and (a*b > largest) ):
				largest = a*b
	print largest
	return 0


if __name__ == '__main__':
	main()

