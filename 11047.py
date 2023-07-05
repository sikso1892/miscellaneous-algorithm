import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [ int(input()) for _ in range(n)][::-1]

cnt = 0 
i = 0

while k > 0:
    if k - coins[i] >= 0:
        cnt = cnt + (k // coins[i])
        k = k % coins[i]
    
    else:
        i = i + 1    

print(cnt)