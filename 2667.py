import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(input())
visited = [[False for _ in range(n)] for _ in range(n)]
r = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visited[i][j]:
            que = [(i,j)]
            cnt = 1
            visited[i][j] = True
            while que:
                _i, _j = que.pop()
                for _ai, _aj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    __i, __j = _i+_ai, _j+_aj
                    if 0<=__i<n and 0<=__j<n and arr[__i][__j]=='1' and not visited[__i][__j]:
                        que.append((__i, __j))
                        visited[__i][__j] = True
                        cnt += 1
            r.append(cnt)

r.sort()
for c in r:
    print(len(r))
    print(c)

            