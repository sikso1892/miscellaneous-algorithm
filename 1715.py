import sys
sys.stdin = open('input.txt', 'r')

import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    heapq.heappush(arr, num)
    
acc = 0

if len(arr) == 1:
    acc = arr[0]

for i in range(n-1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    acc = acc + a + b
    heapq.heappush(arr, a+b)
    

print(acc)