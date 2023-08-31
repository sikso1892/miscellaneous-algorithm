import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    _str = input().strip()
    arr.append(_str)

visited = [[ False for _ in range(m)] for _ in range(n)]

que = [(0,0,0)]
visited[0][0] = True

while que:

    y, x, step = que.pop(0)    
    print(y,x)
    if y == n-1 and x == m-1:
        print(step+1)
        break

    for a,b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        _y = y + a
        _x = x + b
        if (0 <= _y < n and 0 <= _x < m) and not visited[_y][_x] and arr[_y][_x] =='1':
            que.append((_y, _x, step+1))
            visited[_y][_x] = True
        




print(arr)