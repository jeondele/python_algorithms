# 프로그래머스 그리디 4번. 구명보트
# 효율성 똥망,, 테스트 1 , 4 , 5 틀림 
people = 	[10, 20, 30, 40, 50, 60, 70, 80, 90] 
limit = 100

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