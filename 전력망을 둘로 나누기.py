def solution(n, wires):
    global cnt
    answer = float('inf')
    
    def dfs(_dict, i):
        global cnt
        for v in _dict[i]:
            if not visited[v]:
                visited[v] = True
                cnt += 1
                dfs(_dict, v)
        
    for i in range(len(wires)):
        edges = wires[:i]+(wires[i+1:])
        visited = [False] * (n+1)
        _dict = { i:[] for i in range(1,n+1)}

        for a, b in edges:
            _dict[a].append(b)
            _dict[b].append(a)
        
        cnt = 1
        visited[1]=True
        dfs(_dict, 1)
        answer = min(answer, abs((n - cnt) - cnt))
        
        
         
            
    return answer