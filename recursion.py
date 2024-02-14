# def fibo(n):
#     if n<=1:
#         return n
#
#     return fibo(n-1)+fibo(n-2)
#
# for i in range(2020):
#     print(fibo(i), end=' ')

a=[0]*40
a[1]=1
def fibo(n):
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]

def fibo_repetition(n):
    c=0
    d=1

    for _ in range(n):

        c,d=d,c+d
    return c

fibo(30)
print(a[10])
print(fibo_repetition(10))