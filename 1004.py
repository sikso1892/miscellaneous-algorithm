import sys
sys.stdin = input('input.txt','r')

import math

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    pl = int(input())
    cnt = 0

    for _ in range(pl):
        cx, cy, r = map(int, input().split())

        dist1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        dist2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)

        if dist1 < r and dist2 < r:
            continue

        elif dist1 < r:
            cnt += 1

        elif dist2 < r:
            cnt += 1
            
    print(cnt)

