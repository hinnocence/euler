#""" sum of primes below 2000000"""

from math import sqrt
sum_i=0
def is_prime(n):
   limit=int(sqrt(n)+1)
   for i in range(2,limit):
      if n%i==0:
         return False
   return True
for i in xrange(2,2000001):
   if is_prime(i):
      sum_i+=i
print sum_i
