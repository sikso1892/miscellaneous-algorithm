import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(key=lambda x: -x)

acc = 0
for i in range(n):
    acc += A[i]*B[i]
    
print(acc)
