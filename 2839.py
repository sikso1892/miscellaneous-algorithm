import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

acc = 0

while n >= 0:
    if n % 5 == 0:
        acc = acc + (n // 5)
        n = 0
        break
    
    n = n - 3
    acc = acc + 1

if n == 0:
    print(acc)
    
else:
    print(-1)

