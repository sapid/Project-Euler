#!/usr/bin/env python
# encoding: utf-8
"""
problem12.py

Created by whimsy on 2013-03-12.

This program should find the first triangle number with >= 500 factors.
"""
from operator import add

def n_divisors (x): # This won't work for perfect squares. Luckily, triangular numbers aren't perfect squares!
   limit = x
   numberOfDivisors = 0
   i = 1
   while i < limit:
      if x % i == 0:
         limit = x / i
         numberOfDivisors += 1
         #print 'lim' + str(limit)
      i += 1
   return numberOfDivisors * 2


def main():
   n = 1
   tn = 1
   while n_divisors(tn) < 500:
      n += 1 # Our triangle number iteration
      #print 'n' + str(n)
      tn = reduce(add, range(1, n)) # Our triangle number
      #print 'tn' + str(tn)
   print tn

if __name__ == '__main__':
   main()