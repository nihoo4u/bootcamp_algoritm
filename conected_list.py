class Node():
    def __init__(self):
        self.name=None
        self.height=None
        self.link=None
def print_it(x):
    global pre,current,head,target
    print(f"['{x.name}',{x.height}]")
    current=x
    while current.link is not None:
        pre=current
        current=current.link
        print(f"['{current.name}',{current.height}]")


def check_it(x):
    global pre,current,head
    current=x
    if current.height<head.height:
        current.link=head
        head=current
        return
    current=head
    while current.link is not None:
        pre=current
        current=current.link

        if x.height<current.height:
            x.link=current
            pre.link=x
            return
    current.link=x



data_array=[["지민",180],["정국",177],["뷔",183],["슈가",175],["진",179],["퀭퀭이",150]]

node=Node()
node.name=data_array[0][0]
node.height=data_array[0][1]
head=node

for x in range(1,len(data_array)):
    node=Node()
    node.name=data_array[x][0]
    node.height=data_array[x][1]
    check_it(node)
    print_it(head)
    print("---------")




