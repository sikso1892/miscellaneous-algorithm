import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = input()
arr = list(map(int, input().split()))

arr.sort()
acc = 0

for i, v in enumerate(arr):
    acc = acc + v * (len(arr) - i)
    
print(acc)
