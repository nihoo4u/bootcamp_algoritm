## improved selection_sort ##
# def selectionSort(ary) :
#     n = len(ary)
#     for i in range(0, n-1) :
#         minIdx = i
#         for k in range(i+1, n) :
#             if (ary[minIdx] > ary[k]) :
#                 ary[k],ary[minIdx]=ary[minIdx],ary[k]
#
#
#     return ary
#
# ## 전역 변수 선언 부분 ##
# dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
#
# ## 메인 코드 부분 ##
# print('정렬 전 -->', dataAry)
# dataAry = selectionSort(dataAry)
# print('정렬 후 -->', dataAry)

import random
def insert_sort(x):
    for i in range(1,len(x)):
        for j in range(i,0,-1):
            if x[j-1] > x[j]:
                x[j-1],x[j]=x[j],x[j-1]
    return x

a=[random.randint(0,200) for _ in range(10)]
print(a)
print(insert_sort(a))


