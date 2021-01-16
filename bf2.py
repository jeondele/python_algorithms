#프로그래머스 완전탐색 2번. 소수찾기
from itertools import permutations
#set 합집합 : | / 차집합 : -  / 교집합 : & 
#원소추가 : add / 원소삭제 : remove / 원소 여러개 추가 : update
def solution(numbers):
    answer = 0
    set_a = set()
    #nl = [i for i in numbers]
    nl = list(numbers)
    for i in range(1, len(nl)+1) :
        set_a |= set((map(int, map(''.join, permutations(nl, i)))))
    for i in set_a :
        if int(i) <= 1 :
            continue
        cnt = 0    
        for s in range(2, int(i)+1) :
            if int(i) % s == 0:
                cnt += 1
            if cnt > 1 :
                break    
        if cnt == 1:
            answer += 1
    return answer