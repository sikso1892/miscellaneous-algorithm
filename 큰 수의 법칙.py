import sys
sys.stdin = open('input.txt', 'r')

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
acc = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += arr[0]
    if m == 0:
        break
    result += arr[1]
    m -= 1
    
print(result)