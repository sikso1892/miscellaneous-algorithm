def solution(bridge_length, weight, truck_weights):
    answer = 0
    tw = truck_weights
    
    br = []
    acc = 0
    time = 0
    
    
    while tw or br:
        
        time += 1
        
        # 다리 지나갔는지 확인
        if br and br[0][1] == bridge_length:
            tt = br.pop(0)
            acc -= tt[0]
        
        # 수용 가능 하면 pop하여 다리에 추가

        if tw and len(br) < bridge_length and acc + tw[0] <= weight:
            t = tw.pop(0)
            br.append([t,0])
            acc += t
        
        # 현재 다리위에 차량 시간 추가
        for i in range(len(br)):
            br[i][1] += 1
     
    return time