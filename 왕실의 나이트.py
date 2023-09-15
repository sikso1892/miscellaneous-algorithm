import sys
sys.stdin = open('input.txt', 'r')

s = input()

arr = ['','a','b','c','d','e','f','g','h']

x = int(s[1])
y = arr.index(s[0])

dx = [1, -1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, 1, -1]

cnt = 0 
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1<=nx<=8 and 1<=ny<=8:
        cnt += 1

print(cnt)