import sys
sys.stdin = open('input.txt','r')

import sys
input = sys.stdin.readline

a, b = input().split()
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

acc = 0
for i in range(0, len(a)):
    num = alpha.index(a[len(a)-i-1])
    acc += (int(b) ** i ) * num

print(acc)