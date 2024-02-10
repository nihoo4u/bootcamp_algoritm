class Node():
    def __init__(self):
        self.data=None
        self.link=None

def print_nodes(start):
    current=start
    if current.data is None:
        return
    print(current.data)
    while current.link is not None:
        current=current.link
        print(current.data)

head,current,pre=None,None,None
array=["다현","정연","쯔위","사나","지효"]
node=Node()
node.data=array[0]
head=node

for datas in array[1:]:
    pre=node
    node=Node()
    node.data=datas
    pre.link=node
print_nodes(head)









