def solution(k, dungeons):
    global answer 
    answer = -1
    visited = [False] * len(dungeons)
    
    def dfs(rest, acc):
        global answer
        answer = max(answer, acc)
        
        for i in range(len(dungeons)):
            _m, _s = dungeons[i]
            if not visited[i] and rest >= _m:
                
                visited[i] = True
                dfs(rest-_s, acc+1)
                visited[i] = False
    
    for i in range(len(dungeons)):
        dfs(k, 0)
        
    return answer