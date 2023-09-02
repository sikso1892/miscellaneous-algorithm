def solution(begin, target, words):
    if target not in words:
        return 0
    
    words.append(begin)
    words.sort()
    q = [(begin, 0)]
    
    while q:
        
        word, step = q.pop(0)
        if word == target:
            return step
        
        for _word in words:
            cnt = 0
            for i in range(len(word)):
                if word[i] != _word[i]:
                    cnt += 1
                    
            if cnt == 1:
                q.append((_word, step+1))
            
         
    return 1