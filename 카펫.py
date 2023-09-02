def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1):
        if yellow%i == 0:
            
            # 약수
            w, h = yellow//i, i
            if  brown == (w+2) * (h+2) - (w*h):
                answer = [w+2,h+2]
                break
    return answer