import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start <= end:
    mid = (start+end)//2
    total = 0
    
    for num in arr:
        if (num - mid) > 0:
            total += (num - mid)
    
    if total > m:
        start = mid + 1
        
    else:
        result = mid
        end = mid - 1
        
print(result)


