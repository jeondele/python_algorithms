#큐에서 popleft() 는 인자 없이 사용  / 넣을 때는 append() 
#stack에서 pop() 은 인자를 받아서 해당 인덱스를 꺼낼 수 있음 / 넣을 때는 똑같이 append()
#스택에서 pop()에 인자 없이 사용한다면 stack[-1]을 반환하는 구조임

#queue의 개념을 단순히 리스트로 사용한 풀이
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time

from collections import deque
#queue 함수를 이용한 풀이 .. 시간초과 뜸
def solution2(bridge_length, weight, truck_weights):
    q = deque([0]*bridge_length)
    answer = 0
    while q :
        q.popleft()
        answer +=1
        if truck_weights :
            if sum(q) + truck_weights[0] <= weight :
                q.append(truck_weights.pop(0))
            else :
                q.append(0)
    return answer




#애초에 잘못된 풀이.. 인자가 queue에 들어올때 묶여서 들어오지 않음
def solution3(bridge_length, weight, truck_weights):
    answer = 0
    idx = 0
    w = 0
    l = 0
    cnt = 0
    re_list = []
    for i in range(len(truck_weights)) :
        if idx == 0 or i > idx : 
            w = truck_weights[i]
            l = 1
            cnt = 1
            for j in range(i+1 , len(truck_weights)):
                w += truck_weights[j]
                l += 1
                idx = j
                cnt += 1
                if (weight < w or bridge_length < l ) :
                    idx -= 1
                    cnt -= 1
                    break
            re_list.append(cnt)  
            w = 0
            l = 0
            cnt = 0 
            if idx == len(truck_weights) -1 :
                break

    for x in re_list :
        answer += bridge_length
        if x > 1 :
            answer += (x-1)
    return answer+1