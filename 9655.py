import sys 
sys.stdin = open('input.txt','r')

#1 - sk
#2 - cy
#3 - sk
#4 - cy
#5 - sk
#6 - cy

a = int(input())

if a%2:
    print('CY')

else:
    print('SK')