def solution(arr):
    answer = []
    temp = ''
    for i in range(len(arr)):
        if temp != arr[i]:
            temp = arr[i]
            answer.append(arr[i])
    return answer