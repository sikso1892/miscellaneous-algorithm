import sys

sys.stdin = open('input.txt', 'r')

import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []
sum_arr =[]
num = 9
_dict={}
for _ in range(n):
    _str = input().strip()
    length = len(_str)
    for i in range(length):
        if _str[i] in _dict.keys():
            _dict[_str[i]] += 10**(length-i-1)
        else:
            _dict[_str[i]] = 10**(length-i-1)

arr = sorted(list(_dict.values()), reverse=True)
acc = 0
cnt = 9
for num in arr:
    acc += num * cnt 
    cnt -= 1

print(acc)