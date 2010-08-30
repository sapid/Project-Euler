#!/usr/bin/env python
# encoding: utf-8
"""
problem14.py

Created by whimsy on 2010-08-29.
Copyright (c) 2010 Will Crawford. All rights reserved.

This program attempts to find the sum of the digits of 2**1000
"""

import sys
import os


def main():
	sum = 0
	digits = list(str(2**1000))
	for i in digits: sum += int(i)
	print str(sum)
	return 0


if __name__ == '__main__':
	main()

