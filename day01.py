import random

num=random.randrange(1,100)
count=0
while True:
    x = int(input("1~100에서의 숫자를 입력하세요"))
    if x==num:
        print("정답입니다")
        break

    if x>num:
        print("값보다 큽니다")
    else:
        print("값보다 작습니다")

    count+=1



