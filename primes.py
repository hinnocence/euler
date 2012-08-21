import sys
primes=[2]
for i in range(3,20):
    for j in primes:
        if i%j==0:
            break
    else:
        primes.append(i)
print primes       
      

