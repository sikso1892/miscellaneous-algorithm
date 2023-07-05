
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))
arr
cnt = 1
_, curr_time = arr.pop(0)

while arr:
    start, end = arr.pop(0)
    if start >= curr_time:
        cnt += 1 
        curr_time = end
        

print(cnt)