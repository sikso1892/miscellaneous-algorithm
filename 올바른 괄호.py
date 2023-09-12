def solution(s):
    answer = True
    
    st = []
    for i in range(len(s)):
        if s[i] == '(':
            st.append('(')
        elif st:
            st.pop()
        else:
            answer = False
            break
    if st:
        answer = False
    return answer