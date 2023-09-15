import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())


# 0 1 2 3 (북 동 남 서) 북 > 서 > 남 > 동 > 북
# print(n, m)
x, y, d = map(int, input().split())
visited = [ [False for _ in range(m)] for _ in range(n)]
visited[x][y] = True

# 0 1 2 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
mat = []

for _ in range(n):
    mat.append(input().split())
    
def turn_left():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1
    
turn_time = 0
count = 1

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    
    if mat[nx][ny] == '0' and not visited[nx][ny]:
        x, y = nx, ny
        turn_time = 0
        visited[nx][ny] = True
        count += 1
        continue
    
    else:
        turn_time += 1
            
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        
        if mat[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)
    
    




