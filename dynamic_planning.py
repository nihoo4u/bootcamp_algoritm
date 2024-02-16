from collections import deque
class G():
    def __init__(self,size):
        self.SIZE=size
        self.graph=[[0] * size for _ in range(size)]
def BFS(z):
    current=z
    nomi=[]
    visited=[False for _ in range(map_size)]
    visited[current]=True

    nomi=deque(nomi)
    nomi.append(current)
    while nomi:
        x=nomi.popleft()
        print(x, end=' ')
        for i in range(map.SIZE):
            if map.graph[x][i]!=0:
                if not visited[i]:
                    nomi.append(i)
                    visited[i]=True


def print_graph(x):
    for i in range(x):
        for j in range(x):
            print(map.graph[i][j], end=' ')

        print()



map_size = 6
map = G(map_size)

name_array = ['A', 'B', 'C', 'D', 'E', 'F']
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5

map.graph[a][b] = 10
map.graph[a][c] = 15
map.graph[b][a] = 10
map.graph[b][c] = 40
map.graph[b][d] = 11
map.graph[b][e] = 50
map.graph[c][a] = 15
map.graph[c][b] = 40
map.graph[c][d] = 12
map.graph[d][b] = 11
map.graph[d][c] = 12
map.graph[d][e] = 20
map.graph[d][f] = 30
map.graph[e][b] = 50
map.graph[e][d] = 20
map.graph[e][f] = 25
map.graph[f][d] = 30
map.graph[f][e] = 25

# print_graph(map_size)
BFS(int(input()))

