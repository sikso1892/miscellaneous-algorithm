import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

r = 0
for _ in range(n):
    c = min(map(int, input().split()))
    r = max(r, c)

print(r)