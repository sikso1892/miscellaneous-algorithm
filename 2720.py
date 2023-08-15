import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

quart, dime, nickel, penny = 25, 10, 5, 1

for i in range(n):
    c = int(input())

    n_quart, n_dime, n_nickel, n_penny = 0, 0, 0, 0
    
    n_quart = c//quart
    c = c%quart

    n_dime = c//dime
    c = c%dime

    n_nickel = c//nickel
    c = c%nickel

    n_penny = c
    print(n_quart, n_dime, n_nickel, n_penny)



