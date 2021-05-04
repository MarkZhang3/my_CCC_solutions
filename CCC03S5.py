from sys import stdin, exit
from collections import deque
input = stdin.readline
def root(n):
    while dsu[n] != n:
        dsu[n] = dsu[dsu[n]]
        n = dsu[n]
    return n 
c, r, d = map(int, input().split())
graph = []
for i in range(r):
    u, v, w = map(int, input().split())
    graph.append((w, u, v))
vis = [0]*(c+1)
for i in range(d):
    vis[int(input())] = 1
vis[1] = 1 
d += 1 
dsu = [i for i in range(c+1)]
graph.sort(reverse = True)
best = 9999999999
path = []
for edge in graph:
    w, u, v = edge
    rootA, rootB = root(u), root(v)
    if rootA != rootB:
        if vis[u]:
            #print(u)
            d -= 1 
            #print(d)
            vis[u] = 0
        if vis[v]:
            #print(v)
            d -= 1 
            #print(d)
            vis[v] = 0
        if w < best:
            best = w 
        dsu[rootB] = rootA
        #path.append(u)
        #path.append(v)
    if d <= 0:
        break
    #print(dsu)
print(best)