import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

arr.sort()

def bs(target, left, right):
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return None

for num in m_arr:
    if bs(num,0,n-1):
        print('yes',end=' ')
    else:
        print('no', end=' ')
    