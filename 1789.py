import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

s = int(input())

acc = 0

for i in range(1, s):
    acc += i
    if acc > s:
        print(i-1)
        break