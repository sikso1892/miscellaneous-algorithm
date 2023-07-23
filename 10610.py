import sys

sys.stdin = open('input.txt', 'r')

import sys

input = sys.stdin.readline

n = list(input().strip())
n.sort()
n = n[::-1]
sum = 0
if '0' not in n:
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(n))