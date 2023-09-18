import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
st = []
for _ in range(n):
    row = input().split()
    st.append(row)

st.sort(key=lambda x: x[1])
print(' '.join(map(lambda x: x[0], st)))