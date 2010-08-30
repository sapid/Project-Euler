#!/usr/bin/env python
# encoding: utf-8
"""
problem14.py

Created by whimsy on 2010-08-29.
Copyright (c) 2010 Will Crawford. All rights reserved.

This program attempts to find the number that produces the
longest sequence based on the following recurrence relation:
f(n):
1		(n==1)
f(n/2)+1	(n%2==0)
f(3n+1)+1 	(n%2==1)
At least, I think that's the correct recurrence relation.
"""

import sys
import os

# We don't care what the numbers in the sequence are... only how many elements.
def sequencer(n):
	if n==1: return 1
	if n%2==0: return (sequencer(n/2) + 1) # Add one each time we cascade.
	else: return (sequencer(3*n + 1) + 1) # Add one each time we cascade.

def main():
	n = 0
	sequences = [0]
	while len(sequences) < 1000000:
		n+=1
		sequences.append(sequencer(n))
	print sequences.index(max(sequences))
	return 0


if __name__ == '__main__':
	main()

