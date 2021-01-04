#프로그래머스 그리디 2번. 조이스틱 
#다시풀어봐야함

def solution(name):
    list =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    answer = 0
    for i in range(len(name)) :
        if name[i] == 'A' :
            continue
        answer += min ( list.index(name[i]) , abs(list.index(name[i])- len(list)))
        
    skip_idx = 0
    for i in range(len(name)) :
        if name[i] == 'A' :
            continue
        answer += min(skip_idx+1 , i-skip_idx)
        skip_idx = i
    return answer
