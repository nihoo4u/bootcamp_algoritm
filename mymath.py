import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        final = time.time()
        print(f"실행시간: {final - start}")
        return result

    return wrapper
def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)
@timer
def combination(n,r):
    '''
    조합함수
    :param n:
    :param r:
    :return:
    '''
    return int(factorial(n)/(factorial(r)*factorial(n-r)))