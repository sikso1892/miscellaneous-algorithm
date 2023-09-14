import sys
sys.stdin = open('input.txt','r')

import math
t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 점이 동일할때
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dist == 0 and r1 == r2 or :
        print(-1)
    
    elif dist == 0 and r1 != r2:
        print(0)

    elif dist == r1 + r2 or dist == abs(r1-r2):
        print(1)
    
    elif abs(r1-r2) < dist < r1 + r2:
        print(2)
    
    else:
        print(0)
    
    