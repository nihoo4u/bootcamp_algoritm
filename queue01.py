

def is_empty():
    global front,rear
    if front==rear:
        return True
    else:
        return False
def is_full():
    global front,rear,size
    if front==-1 and rear==size-1:
        return True
    else:
        while front!=-1:
            for x in range(front+1,rear+1):
                queue[x-1],queue[x]=queue[x],queue[x-1]
            front-=1
            rear-=1


def enqueue(x):
    global front,rear
    if is_full():
        print("bulged")
        return
    else:
        rear+=1
        queue[rear]=x

def dequeue():
    global front,rear
    if is_empty():
        print('it is empty')
        return
    else:
        queue[front+1]=None
        front+=1

front=-1
rear=-1
size=int(input("input the size"))
queue = [None for _ in range(size)]
while True:
    a=input('input the keyboard')

    if a=='x':
        break
    if a=='e':
        b=input("input the value")
        enqueue(b)
        print(queue)
    elif a=='d':
        dequeue()
        print(queue)