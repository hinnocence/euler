i,j,m,max_m=0,0,0,0
for i in range(100,1000):
   for j in range(100,1000):
      if i>=j:
         m=i*j
         if list(str(m))==list(reversed(str(m))):
           if max_m<=m:
              max_m=m
print max_m
