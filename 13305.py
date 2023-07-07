import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n_city = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))

price = oil[0] * dist[0]
min_oil = oil[0]

for i in range(1, n_city - 1):
    if oil[i] < min_oil:
        min_oil = oil[i]
        
    price += dist[i] * min_oil
    
print(price)