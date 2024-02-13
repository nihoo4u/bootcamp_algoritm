import random
class Node():
    def __init__(self):
        self.data=None
        self.link=None
def print_it(start):
    global pre,current,head ,num,zero
    current=start
    while current.link is not head:
        print(current.data,end=' ')
        current=current.link
    print(current.data)

data_list=[random.randint(-100,100) for _ in range(7)]
print(data_list)

node=Node()
node.data=data_list[0]
head=node
num=0
zero=0
for z in data_list[1:]:
    pre=node
    node=Node()

    if z<0:
        num+=1
        z*=-1
    elif z>0:
        z*=-1
    else:
        zero+=1
    node.data=z




    pre.link=node
    node.link=head



print_it(head)
print(f"음수의 개수:{num}, 0의 개수:{zero}, 양수의 개수: {7-zero-num}")

