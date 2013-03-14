#!/usr/bin/env python
# encoding: utf-8
"""
problem14.py

Created by whimsy on 2013-03-12

This program finds the number of routes from (0, 0) to (n, n) in an n x n grid
where the only valid moves increase one of the coordinates by one.
It solves the same problem using combinatorics, also.
"""
from math import factorial as fact
def combinatorial(n): # This is the combinatorial solution.
   r = 2*n # row 
   c = n # column
   return (fact(r)/ # r choose n
           (fact(c) * fact(r-c)))

def dynamic(gridSize):
   # If the grid is nxn, the number of gridpoints is (n+1)x(n+1)
   grid = [[0 for i in range(gridSize+1)] for j in range(gridSize+1)]
   i = 0
   while i < gridSize: # Boundary conditions
      grid[i][gridSize] = 1
      grid[gridSize][i] = 1
      i += 1
   i = gridSize -1
   while i >= 0: 
      j = gridSize - 1
      while j >= 0: # Here, we basically compute Pascal's Triangle.
         grid[i][j] = grid [i+1][j] + grid[i][j+1]
         j -= 1
      i -= 1
   return grid[0][0]
if __name__=='__main__':
   print combinatorial(20)
   print dynamic(20)