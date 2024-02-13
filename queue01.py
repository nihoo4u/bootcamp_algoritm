def is_empty():
    global front,rear
    if front==rear:
        return True
    else:
        return False
def is_full():
    global front,rear,size
    if (rear+1)%size==front:
        return True


def enqueue(x):
    global front,rear
    if is_full():
        print("bulged")
        return
    else:
        rear=(rear+1)%size
        queue[rear]=x

def dequeue():
    global front,rear
    if is_empty():
        print('it is empty')
        return
    else:
        queue[(front+1)%size]=None
        front=(front+1)%size

front=0
rear=0
size=int(input("input the size"))
queue = [None for _ in range(size)]
while True:
    a=input('input the keyboard')

    if a=='x':
        break
    if a=='e':
        b=input("input the value")
        enqueue(b)
        print("front: ",front,"rear: ",rear)
        print(queue)
    elif a=='d':
        dequeue()
        print("front: ",front,"rear: ",rear)

        print(queue)