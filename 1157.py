_str = input()

dic ={}

for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    dic[c]=0

_str = str.upper(_str)

for i in _str:
    dic[i] += 1

arr = list(dic.keys())

arr.sort(key=lambda x: -dic[x])

if len(arr)>1 and dic[arr[0]] == dic[arr[1]]:
    print('?')

else:
    print(arr[0])