a, b = 0, 1
c = 0
while b < 4000000:
     b, a = a, a + b
     if b % 2 == 0:
          c = c + b
print c
