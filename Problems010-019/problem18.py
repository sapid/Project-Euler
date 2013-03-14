import sys
from os.path import dirname

def main():
   f = open(dirname(sys.argv[0]) + '/problem18.txt', 'r')
   i = 0
   t = [[] for line in range(15)]
   for line in f: # read in the triangular matrix
      t[i] = line.rstrip('\n').split(' ')
      i += 1
   f.close()
   for i in range(t.__len__()):
      for j in range(t[i].__len__()):
         if i - 1 < 0: # no math for first row
            continue
         a=0
         b=0
         if j-1 >= 0: # if j < 0, we get an index error in the previous row.
            a = t[i-1][j-1]
         if j < len(t[i-1]):
            b = t[i-1][j] 
         t[i][j] = int(t[i][j]) + max(int(a), int(b))
   return max(t[i])

if __name__ == '__main__':
   print 'The maximum path through this triangular matrix is ' + str(main())