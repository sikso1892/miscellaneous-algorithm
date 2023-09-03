import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())

posi = []
nega = []

for _ in range(n):
    num = int(input())
    if num > 0:
        posi.append(num)
    else:
        nega.append(num)
    
posi.sort(reverse=True)
nega.sort()

print(posi)
print(nega)
acc = 0
if len(posi) % 2 == 0:
    for i in range(0, len(posi), 2):
        if posi[i+1] == 1:
            acc += posi[i] + posi[i+1]
        else:
            acc += posi[i] * posi[i+1]
else:
    for i in range(0, len(posi)-1, 2):
        if posi[i+1] == 1:
            acc += posi[i] + posi[i+1]
        else:
            acc += posi[i] * posi[i+1]
    
    acc += posi[-1]

if len(nega) % 2 == 0:
    for i in range(0, len(nega), 2):
        acc += nega[i] * nega[i+1]
else:
    for i in range(0, len(nega)-1, 2):
        acc += nega[i] * nega[i+1]
    acc += nega[-1]
    
print(acc)




    