import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

w = int(input())

if w % 2 == 0 and w != 2:
    print('YES')
else:
    print('NO')
    