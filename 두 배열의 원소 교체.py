import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort(reverse=True)
arr2.sort(reverse=True)

arr3 = arr2[:k] + arr1[:n-k] 
print(arr3)
print(sum(arr3))