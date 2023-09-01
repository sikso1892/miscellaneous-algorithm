import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())
nodes = [ [] for i in range(n+1)]
visited = [ False for i in range(n+1) ]
e = int(input())
for _ in range(e):
    v1, v2 = map(int, input().split())
    nodes[v1].append(v2)
    nodes[v2].append(v1)

q = [1]
visited[1] = True
r = 0
while q:
    node = q.pop(0)
    for _node in nodes[node]:
        if not visited[_node]:
            q.append(_node)
            visited[_node] = True
            r += 1

print(r)