def solution(answers):
    answer = []
    
    fst = [1,2,3,4,5]
    snd = [2,1,2,3,2,4,2,5]
    trd = [3,3,1,1,2,2,4,4,5,5]
    
    fst_scr = snd_scr = trd_scr = 0
    for i, ans in enumerate(answers):
        
        if fst[i%5] == ans:
            fst_scr += 1
        if snd[i%8] == ans:
            snd_scr += 1
        if trd[i%10] == ans:
            trd_scr += 1
        
    max_scr = max(fst_scr, snd_scr, trd_scr)
    
    for i, scr in enumerate([fst_scr, snd_scr, trd_scr], 1):
        if max_scr == scr:
            answer.append(i)
    
    return answer