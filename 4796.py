import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline
num = 1
while True:
    L, V, P = map(int, input().split())
    if L == V == P == 0:
        break
    result = (P // V)*L
    if P%V < L:
        result += P%V
    else:
        result += L
    print(f'Case {num}: {result}')
    num += 1
        