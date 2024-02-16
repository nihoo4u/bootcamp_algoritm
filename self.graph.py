class G():
    def __init__(self,size):
        self.SIZE=size
        self.graph=[[0]*size for _ in range(size)]



def print_map():
    print('',end='  ')
    for x in range(map_size):
        print(chr(ord('A')+x).format(2),end=' ')
    print()
    for x in range(map_size):
        print(chr(ord('A')+x).format(2),end=' ')
        for y in range(map_size):
            print(str(map.graph[x][y]).format(2),end=' ')
        print()

def find_it(x): #next의 위치
    stack = []
    visited = []
    current=0
    stack.append(current)
    visited.append(current)
    while len(stack)!=0:
        next=None
        for i in range(map_size):
            if map.graph[current][i]!=0:
                if i  in visited:
                    pass
                else:
                    next=i
                    break
        if next is not None:
            current=next
            stack.append(next)
            visited.append(next)
        else:
            stack.pop()
            if len(stack)==0:
                continue
            current=stack[-1]
    if x in visited:
        return True
    else:
        return False
# def dfs_findit(x):

def explore(x):
    stack=[]
    visited=[]
    current=x
    print(current)
    stack.append(current)
    visited.append(current)
    while len(stack)!=0:
        next=None
        for i in range(map_size):
            if map.graph[current][i]!=0:
                if i is not visited:
                    next=i
                    print(next)
                    stack.append(next)
                    visited.append(next)
                    break

        if next is None:
            stack.pop()
            if len(stack) ==0:
                continue
            current=stack[-1]
        else:
            current=next











map_size=6
map=G(map_size)

name_array=['A','B','C','D','E','F']
a,b,c,d,e,f=0,1,2,3,4,5

map.graph[a][b]=10; map.graph[a][c]=15
map.graph[b][a]=10; map.graph[b][c]=40; map.graph[b][d]=11; map.graph[b][e]=50
map.graph[c][a]=15; map.graph[c][b]=40; map.graph[c][d]=12
map.graph[d][b]=11; map.graph[d][c]=12;map.graph[d][e]=20; map.graph[d][f]=30
map.graph[e][b]=50; map.graph[e][d]=20;map.graph[e][f]=25
map.graph[f][d]=30; map.graph[f][e]=25

cost=[]
for x in range(map_size):
    for y in range(map_size):
        cost.append([map.graph[x][y],x,y])
cost.sort(reverse=True)
real_cost=[]
for x in range(0,len(cost),2):
    if cost[x][0]==0:
        continue
    real_cost.append(cost[x])
index=0
print(real_cost)
while len(real_cost)>map.SIZE-1:
    loss=real_cost[index][0]
    start=real_cost[index][1]
    end=real_cost[index][2]
    map.graph[start][end]=0
    map.graph[end][start]=0
    if find_it(start) and find_it(end):
        del real_cost[index]
    else:
        map.graph[start][end] = loss
        map.graph[end][start] = loss
        index+=1


# explore(0)
total=0
for i in range(map_size):
    total+=sum(map.graph[i])

print(total//2)
