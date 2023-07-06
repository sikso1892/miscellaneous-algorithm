
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

eq = input()
nums = eq.split('-')
acc = 0

lx = sum(map(int, (nums[0].split('+'))))
if nums[0] == '-':
    acc -= lx
else:
    acc += lx

for rx in nums[1:]:
    rx = sum(map(int, (rx.split('+'))))
    acc -= rx
    
print(acc)