import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

n, m = map(int, input().split())
mat = []

for _ in range(n):
    mat.append(input())

q = deque()

q.append((0,0,1))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
while q:
    x, y, step = q.popleft()
    print(x,y,step)
    if x == n-1 and y == m-1:
        print(step)
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and mat[nx][ny] == '1':
            visited[nx][ny] = 1
            q.append((nx,ny,step+1))
