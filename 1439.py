import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import sys
input = sys.stdin.readline

arr = list(input())

cnt = 0

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        cnt += 1
result = (cnt+1)//2
print(result)
