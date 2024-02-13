
## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end = ' ')
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
    print()

def deleteNode(deleteData) :
    global memory, head, current, pre, last
    if head.data == deleteData :

        current = head
        while current.link is not head:
            current=current.link
        temp=head
        head=head.link
        current.link=head



        del(temp)
        return


    current = head                          # 첫 번째  외 노드 삭제
    while current.link != head :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return

def find_node(find_data):
    current=head

    while current.link is not head:
        if current.data==find_data:
            print(current.data)
        current=current.link



## 전역 변수 선언 부분 ##
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

    node = Node()			# 첫 번째 노드
    node.data = dataArray[0]
    head = node
    node.link=head

    for data in dataArray[1:] :		# 두 번째 노드부터
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link=head





    deleteNode("다현")
    find_node('지효')
    # deleteNode("사나")
    printNodes(head)


