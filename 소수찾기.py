import itertools
def solution(numbers):
    a = 0
    
    arr = []
    for i in range(1, len(numbers)+1):
        arr.extend(itertools.permutations(numbers,i))
    arr = set(map(int, map(''.join, arr)))
    
    # c = [True] * (max(arr)+1)
    # c[0] = c[1] = False
    # for i in range(2, max(arr)+1):
    #     for j in range(i+i, max(arr)+1, i):
    #         c[j] = False
    
    # for i in arr:
    #     if c[i]:
    #         a += 1
    
    for num in arr:
        if num < 2:
            continue
            
        flag = True
        
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                flag = False
                break
                
        if flag:
            a += 1
    
    return a