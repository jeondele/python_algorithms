# 프로그래머스 그리디 4번. 구명보트
# people이 50000.. 그렇다면 O(n^2) 는 안됨 -> for문 한번만 써야한다는 생각.
# 2명이상 태울 수 없다.. -> 문제 잘 읽기
# pop, del 등은 시간을 많이 잡는다,, 되도록 안쓰려고 노력해야함.
people = 	[10, 20, 30, 40, 50, 60, 70, 80, 90] 
limit = 100

def solution_final(people, limit) :
    answer = 0
    sorted_people = sorted(people)
    i , j = 0 , len(sorted_people)-1
    while i <= j :
        answer += 1
        if sorted_people[i] + sorted_people[j] <= limit :
            i += 1
            j -= 1
        else :
            j -= 1
    return answer

def solution3(people, limit) :
    answer = 0
    sorted_people = sorted(people, reverse = True)
    visited = [False]*len(sorted_people)
    for i in range(len(sorted_people)):
        if visited[i] == True :
            continue
        answer += 1
        visited[i] = True
        tmp_limit = limit - sorted_people[i]
        for j in range(i+1 , len(sorted_people)) :
            if visited[j] == True :
                continue
            if tmp_limit - sorted_people[j] >= 0 :
                tmp_limit -= sorted_people[j]
                visited[j] = True 
                break
    return answer

def solution2(people, limit) :
    answer = 0
    sorted_people = sorted(people, reverse = True)
    visited = [False]*len(sorted_people)
    for i in range(len(sorted_people)):
        if visited[i] == True :
            continue
        answer += 1
        visited[i] = True
        tmp_limit = limit - sorted_people[i]
        print(tmp_limit)
        for j in range(i+1 , len(sorted_people)) :
            print( str(j) + '번째 :: ' + str(tmp_limit - sorted_people[j]))
            if tmp_limit - sorted_people[j] >= 0 :
                print('방문???' + str(j) + '번째')
                tmp_limit -= sorted_people[j]
                visited[j] = True 
                continue

    return answer


def solution(people, limit) :
    answer = 0
    sorted_people = sorted(people, reverse = False)
    #print(sorted_people)
    while sorted_people :
        print(sorted_people)
        answer += 1
        print(sorted_people[-1])
        left_weight = limit - sorted_people.pop()
        
        print(left_weight)    
        idx = 0
        while left_weight > 0 :
            
            idx += 1
            if idx > len(sorted_people) :
                break
            print(str(idx)+ ' 번째 '+ str(sorted_people[-idx]))
            if left_weight - sorted_people[-idx] >= 0 :
                print('뽑는 애 :: ' + str(sorted_people[-idx]))
                left_weight -= sorted_people.pop(-idx)
                idx -= 1
    return answer

print(solution(people, limit))