import sys
sys.stdin = open('input.txt','r')

n, t = map(int, input().split())

time = []
for _ in range(n):
    s, l, c = map(int, input().split())
    if s+l*(c-1) < t:
        continue

    start = 0
    end = c-1
    result = 0

    while start <= end:
        mid = (start+end)//2
        nt = s+l*mid
        
        if nt >= t:
            result = nt
            end = mid-1
        
        else:
            start = mid+1

    time.append(result-t)

if time:
    print(min(time))

else:
    print(-1)