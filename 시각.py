import sys
sys.stdin = open('input.txt', 'r')

cnt = 0
h = int(input())
for h in range(h+1):
    for m in range(60):
        for s in range(60):
            d = str(h)+str(m)+str(s)
            if '3' in d:
                cnt += 1
print(cnt)