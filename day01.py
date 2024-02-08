def add_it(x):
    a.append(x)
def insert_it(x,y):
    a.append(None)
    for i in range(len(a)-1,x,-1):
        a[i],a[i-1]=a[i-1],a[i]
    a[x]=y





a=[1,2,3,4]
insert_it(2,10)
print(a)

