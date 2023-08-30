import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

visited = [0] * (n+1)

ans = []
def recursive_dfs(v):
    global graph, visited
    visited[v] = 1
    ans.append(v)
    for node, edge in enumerate(graph[v]):
        if edge and visited[node] == 0:
            recursive_dfs(node)
recursive_dfs(v)
print(' '.join(map(str, ans)))

ans = []
visited = [0] * (n+1)
def bfs(v):
    global graph, visited
    que = [v]
    visited[v] = 1
    ans.append(v)
    while que:
        _v = que.pop(0)
        for node, edge in enumerate(graph[_v]):
            if edge and visited[node] == 0:
                visited[node] = 1
                ans.append(node) 
                que.append(node)
bfs(v)
print(' '.join(map(str, ans)))
