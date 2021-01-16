#프로그래머스 완전탐색 2번. 소수찾기
from itertools import permutations
#set 합집합 : | / 차집합 : -  / 교집합 : & 
#원소추가 : add / 원소삭제 : remove / 원소 여러개 추가 : update
def solution(numbers):
    answer = 0
    set_a = set()
    #for 문 안쓰고 리스트로 감싸면 바로 만들수 있음
    #nl = [i for i in numbers]
    nl = list(numbers)
    for i in range(1, len(nl)+1) :
        set_a |= set((map(int, map(''.join, permutations(nl, i)))))
    for i in set_a :
        if int(i) <= 1 :
            continue
        cnt = 0    
        #for s in range(2, int(i)+1) :
        #    if int(i) % s == 0:
        #        cnt += 1
        #    if cnt > 1 :
        #        break    
        #if cnt == 1:
        #    answer += 1
        #루트한 값만 for문을 돌리면 시간복잡도를 줄일 수 있음
        for s in range(2, int(int(i)**0.5) +1) :
            if int(i) % s == 0:
                cnt += 1
                break    
        if cnt == 0:
            answer += 1
    return answer