import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))


arr.sort()
acc = 0

for i, v in enumerate(arr):
    acc = acc + v * (len(arr) - i)
    
print(acc)
