import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

arr = [0] * 10001

def d(n):
    global arr
    if n > 10000:
        return
    
    if arr[n] > 2:
        return
    
    arr[n] += 1

    next_n = n 
    for c in str(n):
        next_n  += int(c)
    d(next_n)
    
for i in range(1, 10001):
    d(i)

for i in range(1,10001):
    if arr[i] == 1:
        print(i)
