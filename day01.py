def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

def combination(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

print(combination(5,2))
