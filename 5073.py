import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline


while True:
    a1, a2, a3 = map(int, input().split())

    b = [a1,a2,a3]
    b.sort()
    
    if b[0] == b[1] == b[2] == 0:
        break
    
    elif b[0] + b[1] <= b[2]:
        print('Invalid')

    elif b[0] == b[1] == b[2]:
        print('Equilateral')
    
    elif b[0] == b[1] or b[0] == b[2] or b[1] == b[2]:
        print('Isosceles')
    
    else:
        print('Scalene')
    

