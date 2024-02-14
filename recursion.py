def fibo(n):
    if memo[n] is not None:
        return memo[n]
    if n<=1:
        return n


    x= fibo(n-1)+fibo(n-2)
    memo[n]=x
    return x

memo=[None]*30

print(fibo(5))
print(memo[5])
