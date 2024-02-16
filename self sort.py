#selecting sort
import random
def selection_sort(x):
    for i in range(len(x)-1):
        index=i
        for j in range(i+1,len(x)):
            if x[j]<x[index]:
                index=j

        x[i],x[index]=x[index],x[i]]]
    return x

def insert_sort(x):
    for i in range(1,len(x)):
        for j in range(i-1,-1,-1):
            if x[i] <x[j]:
                x[i],x[j]=x[j],x[i]

    return x



a=[random.randint(100,200) for _ in range(20)]
print(a)
print(selection_sort(a))
print(insert_sort(a))






