#!/usr/bin/env python
# encoding: utf-8
"""
problem17.py

Created by whimsy on 2010-08-29.
This program finds how many letters are in the string composed of the 
words representing the numbers 1-1000 by brute force.
TODO: Optimize.
"""


def main():
   ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
   tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
   teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
   hugestring = ''
   last = ''
   for i in range(1, 1000 + 1):
      current = list(str(i))
      if len(current) == 1:
         hugestring+=ones[int(current[0])]
         continue
      if len(current) == 2:
         if current[0] == '1': #teens case
            hugestring += teens[int(current[1])]
            continue
         else:
            hugestring += tens[int(current[0])]
            hugestring += ones[int(current[1])]
            continue
      if len(current) == 3:
         hugestring += ones[int(current[0])] + 'hundred'
         if current[1] == '0' and current[2] == '0':
            continue
         hugestring += 'and'
         if current[1] == '1': # teens.
            hugestring += teens[int(current[2])]
         else:
            hugestring += tens[int(current[1])]
            hugestring += ones[int(current[2])]
      last = hugestring[-15:]

   hugestring+='onethousand'
   return len(hugestring)


if __name__ == '__main__':
   print 'The number of letters in the string ' \
         'composed of the words representing 1-1000 inclusive is ' + str(main())

