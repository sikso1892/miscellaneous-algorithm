import sys
sys.stdin=open('input.txt','r')

def qsort(arr):
    if len(arr) <=1:
        return arr
    
    p = arr[0]
    t = arr[1:]
    
    l = [x for x in t if x >= p]
    r = [x for x in t if x < p]
    
    return qsort(l) + [p] + qsort(r)

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
print(' '.join(map(str, qsort(arr))))
    