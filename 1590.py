import sys
sys.stdin = open('input.txt','r')

n, t = map(int, input().split())

bus = []
for _ in range(n):
    bus.append(list(map(int, input().split())))

bus_time = []
for si, li, ci in bus:
    for time in range(si, si+li*ci, li):
        if t <= time:
            bus_time.append(time-t)
            break

if bus_time:
    print(min(bus_time))
else:
    print(-1)