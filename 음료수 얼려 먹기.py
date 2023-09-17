import sys
sys.stdin=open('input.txt','r')

n, m = map(int, input().split())

mat = []
visited = [[0]*m for _ in range(n)]

for _ in range(n):
    mat.append(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m and mat[nx][ny] == '0' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny)

cnt = 0
for i in range(n):
    for j in range(m):
        
        if visited[i][j] == 0 and mat[i][j]=='0':
            visited[i][j] = 1
            cnt +=1
            dfs(i,j)
            
print(cnt)