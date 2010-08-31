#!/usr/bin/env python
# encoding: utf-8
"""
Problem2.py
Created for Project Euler
Created by whimsy on 2010-04-26.
Copyright (c) 2010 Will Crawford. All rights reserved.

This program is intended to...
Find the sum of all the even-valued terms in the sequence which do not exceed four million.
"""

import sys
import os

phi = (1 + 5**0.5) / 2

def fib(n):
	return int(round((phi**n - (1-phi)**n) / 5**0.5))

def main():
	j = 0
	i=0
	while fib(i) < 4000000:
		if fib(i)%2==0:
			j=j+fib(i)
		i=i+1
	print j
	return 0

if __name__ == '__main__':
	main()

