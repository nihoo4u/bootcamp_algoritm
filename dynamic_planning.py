import sys
def DFS():
    count=0
    current=1
    stack=[]
    visited=[False]*(n+1)
    stack.append(current)
    visited[current]=True
    while stack:
        next=None
        for i in node[current]:
            if not visited[i]:
                current=i
                visited[i]=True
                stack.append(i)
                count+=1
                next=current
                break

        if next is None:
            stack.pop()
            if not stack:
                continue
            current=stack[-1]



    return count





n=int(input())
m=int(input())
node=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)

print(DFS())