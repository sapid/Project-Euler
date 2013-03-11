#!/usr/bin/env python
# encoding: utf-8
"""
problem13.py

Created by whimsy on 2013-03-11.

This program should read in large numbers, add 
them, and return the first ten digits of the sum.
"""
import sys
from os.path import dirname


def main():
   f = open(dirname(sys.argv[0]) + '/problem13.txt', 'r')
   sum = 0
   for line in f:
      sum += long(line)
   print str(sum)[:10]
   return 0

if __name__ == '__main__':
   main()