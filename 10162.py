import sys

sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

T = int(input())

A=300 
B=60 
C=10

n_A, n_B, n_C = 0,0,0

if T%C:
    print(-1)

else:
    while T > 0:
        if T // A :
            n_A = T//A
            T = T%A
            
        elif T//B:
            n_B = (T//B)
            T = T%B
            
        elif T//C:
            n_C = (T//C)
            T = T%C
            
    if T == 0 :
        print(n_A, n_B, n_C)
        
    else:
        print(-1)