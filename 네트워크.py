def solution(n, computers):
    global visited
    answer = 0
    visited = [ False for i in range(n)]
    
    def bfs(s):
        global visited
        que = [s]
        visited[s] = True
        while que:
            node = que.pop(0)
           
            for i in range(n):
                if i != node and computers[node][i] and not visited[i]:
                    que.append(i)
                    visited[i] = True
                    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer