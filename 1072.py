import sys
sys.stdin = open('input.txt', 'r')

import math
x, y = map(int, input().split())

z = y * 100 // x

if z >= 99:
    print(-1)
    exit()

cnt = 0

start = 0
end = x
result = end
while start <= end:
    mid = (start + end) //2
    nz = (y+mid)*100//(x+mid)
    if nz != z:
        result = mid
        end = mid -1
    else:
        start = mid + 1

print(result)