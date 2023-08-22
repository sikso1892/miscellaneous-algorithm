import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())
dp = [float('inf')] * 5001

dp[3] = 1
dp[5] = 1

if n <= 5:
    print(dp[n])
else:
    for i in range(6, n+1):
        dp[i] = min(dp[i-3], dp[i-5])+1

if dp[n] >= float('inf'):
    print(-1)
else:
    print(dp[n])