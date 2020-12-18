#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion  = ['josipa', 'filipa', 'marina', 'nikola']

#나의 풀이

def solution(participant, completion):
    hash_participant = {}
    answer = ""
    for person in participant :
        if person in hash_participant.keys() :
            hash_participant[person] += 1
        else :
            hash_participant[person] = 1
    for person in completion :
        if person in hash_participant.keys() :
            hash_participant[person] -= 1
    for person in hash_participant.keys() :
        if hash_participant[person] == 1 :
            answer = person 
    return answer

#### 다른 사람 풀이

##### import collections 의 counter 를 쓰면 알아서 해시맵 완성 됨 + 차집합 , 합집합 , 교집합 기능 도 있음 

import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


print(solution(participant, completion))