import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

cnt = 0
for _ in range(n):
    word = input()
    se = set(word[0])
    flag = True

    for i in range(1, len(word)):
        if word[i-1] != word[i]:
            if word[i] in se:
                flag = False
                break
            else:
                se.add(word[i])
    if flag:
        cnt+=1

print(cnt)

        
        