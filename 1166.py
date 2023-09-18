import sys
sys.stdin = open('input.txt', 'r')

n, l, w, h = map(int, input().split())

lef = 0
rig = max(l,w,h)


for _ in range(10000):
    A = (lef+rig)/2
    print(A, lef, rig)
    cnt = (l//A) * (w//A) * (h//A)
    if cnt < n:
        rig = A
    else:
        lef = A
    
print(lef)