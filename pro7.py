import sys
primes=[2]
for i in range(3,200000):
    for j in primes:
        if i%j==0:
            break
    else:
        primes.append(i)
        if len(primes)>=10001:
            break
      
print primes[10000]
