import itertools
def solution(numbers):
    answer = '0'
    
    arr = sorted(map(str, numbers), key = lambda x: x*3, reverse=True)
    answer = ''.join(arr)
    answer = str(int(answer))
    return answer