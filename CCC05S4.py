from sys import stdin, exit
from collections import deque
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    dfs = deque([input().strip() for i in range(n)])
    graph = {dfs[-1]:[]}
    stack = deque([dfs[-1]])
    #print(stack)
    while stack:
        if len(stack) >= 2:
            cur = dfs.popleft()
            #print(cur, stack)
            if cur == stack[-2]:
                stack.pop()
            else:
                graph[cur] = [] 
                graph[stack[-1]].append(cur)
                stack.append(cur)
        else:
            if dfs:
                cur = dfs.popleft()
                graph[stack[-1]].append(cur)
                graph[cur] = []
                stack.append(cur)
            else:
                break
    #print(graph)
    t = 0
    while stack:
        for i in range(len(stack)):
            cur = stack.popleft()
            for j in graph[cur]:
                stack.append(j)
        t += 1 
    ans = (n-(t-1)*2)*10
    if ans >= 0:
        print(ans)
    else:
        print(0)