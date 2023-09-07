import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
st = []

while a:
    st.append(a%b)
    a = a // b 


acc = ''
for i in st[::-1]:
    acc += alpha[i]
    
print(acc)