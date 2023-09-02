def solution(maps):
    answer = 0
    q = [(0,0,1)]
    
    n_row = len(maps)
    n_col = len(maps[0])
    
    visited = [[False for _ in range(n_col)] for _ in range(n_row)]
    visited[0][0] = True
    flag = False
    
    while q:
        y,x, step = q.pop(0)
        
        if y == n_row - 1 and x == n_col -1 :
            flag = True
            answer = step
            break
            
        for ay, ax in [(1,0), (-1,0), (0,1), (0, -1)]:
            if 0 <= y+ay < n_row and 0 <= x+ax < n_col and not visited[y+ay][x+ax] and maps[y+ay][x+ax] == 1:
                visited[y+ay][x+ax] = True
                q.append((y+ay, x+ax, step+1))
                
        
        
    if not flag:
        answer = -1
        
    return answer