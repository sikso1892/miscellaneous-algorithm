import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

def bs(arr, s, e, t):
    while s <= e:
        mid = (s + e)//2
        if arr[mid] == t:
            return mid
        
        if arr[mid] < t:
            s = mid + 1

        else:
            e = mid -1

    return None

for num in b:
    if bs(a, 0, len(a)-1, num) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
