
## insert_sort
# import random
# def insert_sort(x):
#     for i in range(1,len(x)):
#         for j in range(i,0,-1):
#             if x[j-1] > x[j]:
#                 x[j-1],x[j]=x[j],x[j-1]
#     return x
#
# a=[random.randint(0,200) for _ in range(10)]
# print(a)
# print(insert_sort(a))

##choice_sort

# import random
# def choice_sort():
#     for i in range(len(a)):
#         index=i
#         for j in range(i+1,len(a)):
#             if a[index]> a[j]:
#                 index=j
#         a[index],a[i]=a[i],a[index]
#
#
#
# a=[random.randint(0,200) for _ in range(10)]
# print(a)
# choice_sort()
# print(a)

## python optimized quick_sort()
import time
import random
import functions_zip
# def quick_sort(x):
#     if len(x)<2:
#         return x
#     pivot=x[0]
#     remn=x[1:]
#     less=[z for z in remn if z<=pivot]
#     more=[z for z in remn if z>pivot]
#     return quick_sort(less) + [pivot] + quick_sort(more)
start=time.time()
a=[random.randint(0,200) for _ in range(10)]
print(a, len(a))
b=functions_zip.quick_sort(a)
print(b,len(b))
end=time.time()
print(end-start)

# import random
# def bubble_sort():
#     for j in range(len(a)-1):
#         ch=False
#         for i in range(1,len(a)-j):
#             if a[i]< a[i-1]:
#                 a[i],a[i-1]=a[i-1],a[i]
#                 ch=True
#         if  not ch:
#             break
#     return a
#
# a=[random.randint(0,200) for _ in range(10)]
# b=sorted(a)
# print('original',a)
# bubble_sort()
# print('by bubble',a)
# print('real answer',a)
# if a==b:
#     print('good')
# else:
#     print('suck')

