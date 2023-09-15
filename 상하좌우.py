import sys
sys.stdin = open('input.txt','r')

n = int(input())
dirs = input().split()

x, y = 1,1
for d in dirs:
    if 'R' == d and 1<=y+1<=n:
        y += 1
    elif 'L' == d and 1<=y-1<=n:
        y -= 1
    elif 'U' == d and 1<=x-1<=n:
        x -= 1
    elif 'D' == d and 1<=x+1<=n:
        x += 1
print(x,y)