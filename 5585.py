import sys

sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())
coins = [500, 100, 50, 10, 5, 1]

i = 0
rest = 1000 - n
cnt = 0 
while rest > 0:
    
    if rest // coins[i] :
        cnt = cnt + rest // coins[i]
        rest = rest % coins[i]
        i = i + 1
        
    else:
        i = i + 1

print(cnt)