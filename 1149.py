import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())
dp = [[0,0,0]for _ in range(n)]
home = []

for i in range(n):
    home.append(list(map(int, input().split())))

dp[0] = home[0]
dp[1][0] = min(home[1][0]+home[0][1], home[1][0]+home[0][2])# RG RB 
dp[1][1] = min(home[1][1]+home[0][0], home[1][1]+home[0][2])
dp[1][2] = min(home[1][2]+home[0][0], home[1][2]+home[0][1])

for i in range(2, n):

    dp[i][0] = home[i][0] + min(dp[i-1][1], dp[i-1][2]) 
    dp[i][1] = home[i][1] + min(dp[i-1][0], dp[i-1][2]) 
    dp[i][2] = home[i][2] + min(dp[i-1][0], dp[i-1][1]) 

print(min(dp[-1]))
