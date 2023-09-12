def solution(priorities, location):
    answer = 0
    arr = []
    
    for i in range(len(priorities)):
        if i == location:
            arr.append((priorities[i], True))
        else:
            arr.append((priorities[i], False))

    while arr:
        flag = False
        p, loc = arr.pop(0)
        

        for i in range(len(arr)):
            if p < arr[i][0]:
                flag = True
                break
                
        if flag:
            arr.append((p, loc))
            continue
            
        elif loc:
            answer += 1
            break
        
        else:
            answer += 1
                
    return answer
