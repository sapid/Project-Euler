#!/usr/bin/env python
# encoding: utf-8
"""
problem16.py

Created by whimsy on 2010-08-29.

This program attempts to find the sum of the digits of 2**1000
"""

import sys
import os


def main():
	sum = 0
	digits = list(str(2**1000))
	for i in digits: sum += int(i)
	print "Sum of the digits of 2**1000: " + str(sum)
	return 0


if __name__ == '__main__':
	main()

