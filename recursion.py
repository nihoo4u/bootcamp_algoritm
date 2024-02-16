# def fibo(n):
#     if memo[n] is not None:
#         return memo[n]
#     if n<=1:
#         return n
#
#
#     x= fibo(n-1)+fibo(n-2)
#     memo[n]=x
#     return x
#
# memo=[None]*50
#
#
# print(fibo(5))
# print(memo[5])

## 함수 선언 부분 ##
# def palindrome(pStr) :
#     if len(pStr) <= 1 :
#         return True
#
#     if pStr[0] != pStr[-1] :
#         return False
#
#     return palindrome(pStr[1:len(pStr)-1])


## 전역 변수 선언 부분 ##
# strAry = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주", "야 너 이번주 주번이 너야", "살금 살금"]

## 메인 코드 부분 ##
# for testStr in strAry :
# 	print(testStr, end = '--> ' )
# 	testStr = testStr.lower().replace(' ','')
# 	if palindrome(testStr) :
# 		print('O')
# 	else :
# 		print('X')

def transfer(x,by):
    if x<by:
        return x


    return str(transfer(x//by,by)) + str(x%by)
print(transfer(65535,8))