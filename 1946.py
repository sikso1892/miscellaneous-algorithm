import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    applicants = [0] * n
    for i in range(n):
        a, b = map(int, input().split())
        applicants[i] = [a, b]
    
    applicants = sorted(applicants, key = lambda x: x[0])
    result = 1
    b_min = applicants[0][1]
    
    for i in range(1, n):
        
        if b_min > applicants[i][1]:
            result += 1
            b_min = applicants[i][1]
    print(result)
            
        