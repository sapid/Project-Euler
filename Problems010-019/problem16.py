#!/usr/bin/env python
# encoding: utf-8
"""
problem16.py

Created by whimsy on 2010-08-29.

This program finds the sum of the digits of 2**1000
"""

def main():
	dsum = 0
	digits = list(str(2**1000))
	for i in digits: dsum += int(i)
	print "Sum of the digits of 2**1000: " + str(dsum)
	return 0


if __name__ == '__main__':
	main()

