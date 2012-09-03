def num_of_fac(i):
    cnt=0
    for x in range(1,i+1):
        if i%x==0:
            cnt+=1
    return cnt
i=1
tri_num=1
while(True):
     if num_of_fac(tri_num)>=500:
         break
     i+=1
     tri_num+=i
     print i
print i 

