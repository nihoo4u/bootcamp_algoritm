class Node():
    def __init__(self):
        self.data=None
        self.link=None

array=[chr(x+96) for x in range(6)]
node1=Node()
node2=Node()
node3=Node()
node4=Node()
node5=Node()

node1.data=array[1]
node2.data=array[2]
node3.data=array[3]
node4.data=array[4]
node5.data=array[5]

node1.link=node2
node2.link=node3
node3.link=node4
node4.link=node5
head=node1

def print_it(x):
    current=x
    print(str(current.data)+"입니다")
    while current.link is not None:
        current=current.link
        print(f"{current.data}입니다")

def insert_it(find_data,inset_data):
    global head,current,pre
    if head.data==find_data:
        node=Node()
        node.data=inset_data
        node.link=head
        head=node
        return

    current=head
    while current.link is not None:
        pre=current
        current=current.link
        if current.data==find_data:
            node=Node()
            node.data=inset_data
            node.link=current
            pre.link=node
            return
    node=Node()
    node.data=inset_data
    current.link=node
def del_it(delete_data):
    global head,current,pre
    if head.data==delete_data:
        current=head
        head=head.link
        del current
        return

    current=head
    while current.link is not None:
        pre=current
        current=current.link
        if current.data==delete_data:
            pre.link=current.link
            del current
            return

insert_it('a','gogo')
print_it(head)
del_it('c')
print("-----c is deleted-----")
print_it(head)
