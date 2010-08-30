#!/usr/bin/env python
# encoding: utf-8
"""
problem20.py

Created by Whimsy on 2010-08-29.
Copyright (c) 2010 Will Crawford. All rights reserved.

This program sums the digits of 100 factorial.
"""

import sys
import os
from math import factorial # Is this cheating?

def main():
	a = list(str(factorial(100)))
	sum = 0
	for i in a:
		sum += int(i)
	print str(sum)
	return 0


if __name__ == '__main__':
	main()

