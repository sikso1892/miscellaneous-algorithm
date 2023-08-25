import sys

sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

h,w,n,m = map(int, input().split())

import math

print (math.ceil(h/(n+1)) * math.ceil(w/(m+1)))
