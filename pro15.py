def mul(a,b): return a*b
chi=reduce(mul,range(1,41))
par=reduce(mul,range(1,21))*reduce(mul,range(1,21))
print chi/par

