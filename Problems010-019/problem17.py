#!/usr/bin/env python
# encoding: utf-8
"""
problem17.py

Created by whimsy on 2010-08-29.

"""

import sys
import os


def main():
	ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	hugestring = ''
	for i in range(1, 1000 + 1):
		current = list(str(i))
		if len(current) == 1:
			hugestring+=ones[int(current[0])]
		if len(current) == 2:
			if current[1] == '1': #teens case
				hugestring += teens[int(current[1])]
			else:
				hugestring += tens[int(current[0])]
				hugestring += ones[int(current[1])]			
		if len(current) == 3:
			hugestring += ones[int(current[0])] + 'hundred'
			if current[1] != '0' and current[2] != '0':
				hugestring += 'and'
			if current[1] == '1': # teens.
				hugestring += teens[int(current[2])]
			else:
				hugestring += tens[int(current[0])]
				hugestring += ones[int(current[1])]

	hugestring+='onethousand'
	print len(hugestring)
	return 0


if __name__ == '__main__':
	main()

