#!/usr/bin/env python
# encoding: utf-8
"""
problem20.py

Created by Whimsy on 2010-08-29.
Copyright (c) 2010 Will Crawford. All rights reserved.

This program sums the digits of factorial(100).
"""

import sys
import os
from math import factorial # Is this cheating?

def _factorial(n): # Just to prove I can do it.
	if n == 1: return 1
	else: return _factorial(n-1) * n
	# Factorials are very, simple, obvious use-cases for recursion.

def main():
	a = list(str(factorial(100)))
	sum = 0
	for i in a:
		sum += int(i)
	print str(sum)
	return 0

if __name__ == '__main__':
	main()
