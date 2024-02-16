#최단거리 k
#출발 x
#최다거리가 k인 도시를 출

import sys
from collections import deque
n,m,k,x=map(int,sys.stdin.readline().rstrip().split())
node=[[] for _ in range(n+1)]
visited=[False]*(n+1)
distance=[0]*(n+1)

for _ in range(m):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    node[a].append(b)
def BFS(x):

    queue=deque()
    queue.append(x)
    visited[x]=True
    while queue:
        x=queue.popleft()
        for i in node[x]:
            if not visited[i]:
                distance[i]=distance[x]+1
                queue.append(i)
                visited[i]=True



BFS(x)
check=False
for i in range(len(distance)):
    if distance[i]==k:
        check=True
        print(i)
if not check:
    print(-1)






