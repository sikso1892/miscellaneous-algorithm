import sys
sys.stdin = open('input.txt', 'r')

# 1 = 1
# 7 - 6 * 1
# 19 - 6 * 2
# 37 - 6 * 3

sin = int(input())

acc = 1
i = 0
if sin == 1:
    print(1)
    exit()
while acc < sin:
    acc += 6 * i
    i += 1

print(i)