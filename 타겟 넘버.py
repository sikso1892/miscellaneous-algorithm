def dfs(i, acc, numbers, target):
    global answer
    if i == len(numbers):
        if acc == target:
            answer += 1
        return
    dfs(i+1, acc+numbers[i], numbers, target)
    dfs(i+1, acc-numbers[i], numbers, target)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0, numbers, target)
    return answer