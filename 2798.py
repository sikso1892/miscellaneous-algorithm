import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# def rec(acc, i, cnt):
#     if i >= len(arr) or acc > m:
#         return 0
    
#     if cnt == 3 and acc <= m:
#         return acc
    
#     for j in range(i, len(arr)):
#         rec(acc, i, cnt)
#         rec(acc, i, cnt)

# answer = rec(0, 0, 0)
answer = 0
for i in range(0, n):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            __sum = sum((arr[i],arr[j],arr[k]))
            if answer < __sum <= m:
                answer = __sum

print(answer)
    