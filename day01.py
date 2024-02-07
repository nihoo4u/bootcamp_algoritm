import copy
x=[[1],2,3]
# x=[1,2,3]
a=x
b=copy.deepcopy(x)
c=x.copy()


print('x',x,id(x[0]))
print('a',a,id(a[0]))
print('b',b,id(b[0]))
print('c',c,id(c[0]))
x[0].append(9)
# x[0]=9

print('x',x,id(x[0]))
print('a',a,id(a[0]))
print('b',b,id(b[0]))
print('c',c,id(c[0]))
