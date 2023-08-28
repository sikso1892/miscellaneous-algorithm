def solution(sizes):
    answer = 0
    w = h = 0
    
    answer = w * h
    for fst, snd in sizes:
        if fst < snd:
            fst, snd = snd, fst
        if w < fst:
            w = fst
        if h < snd:
            h = snd
    answer = w * h
    
    return answer