import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = []
for _ in range(n):
    x,y = map(int, input().split())
    arr.append([x,y])

arr.sort()
for x,y in arr:
    print(x,y)