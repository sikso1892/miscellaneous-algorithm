import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[False for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = True

    for y in range(n):
        for x in range(m):
            if not visited[y][x] and arr[y][x]:

                q = [(y,x)]
                cnt += 1
                print((y,x))
                while q:
                    _i, _j = q.pop(0)
                    for _ay, _ax in [(1,0), (-1,0), (0,1), (0,-1)]:
                        _y, _x = _i+_ay, _j+_ax
                        if 0<=_x<m and 0<=_y<n and not visited[_y][_x] and arr[_y][_x]:
                            visited[_y][_x] = True
                            q.append((_y,_x))
    print(cnt)             
                

