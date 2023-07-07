import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())
ropes = [ int(input()) for _ in range(n) ]

ropes.sort(key=lambda x: -x)

acc = 0
for i, w in enumerate(ropes, 1):
    if acc <= i * w:
        acc = i * w

print(acc)