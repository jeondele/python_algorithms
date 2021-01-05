#프로그래머스 그리디 3번. 큰 수 만들기

from itertools import combinations
number = '4177252841'
k = 4
#너무도 깔끔한 풀이.. 언제쯤 이렇게 짜지?
def solution_best(number, k):
    stack = []
    for num in number :
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

def solution_final(number, k):
    answer = []
    cnt = 0
    for i in range(len(number)) :
        if cnt == k :
            return ''.join(answer) + number[i:]
        if i == 0 or number[i] <= number[i-1] :
            if len(answer) == len(number) - k :
                continue
            answer.append(number[i])    
        else :
            while (answer and answer[len(answer)-1] < number[i] and cnt < k  ) :
                #print(answer)
                answer.pop(len(answer)-1)
                cnt += 1
            answer.append(number[i])
      
    return ''.join(answer) 

def solution(number, k):
    answer_list = []
    num_list = list(number)
    cb_list = list(combinations(num_list, k))
    min(cb_list)
    for cb in cb_list :
        for i in list(cb) :
            num_list.remove(i)
        answer_list.append(''.join(num_list))
        num_list = list(number)    
    return max(answer_list)

#combination을 이용한 풀이... 모두 시간초과 뜸.. 
def solution2(number, k):
    answer = ''
    num_list = list(number)
    cb_list = list(combinations(num_list, k))
    for cb in cb_list :
        for i in cb :
            num_list.remove(i)
        tmp_answer = ''.join(num_list)    
        if answer == '' or answer < tmp_answer :
            answer = tmp_answer
        num_list = list(number)    
    return answer 

def solution3(number, k):
    answer_list = []
    num_list = list(number)
    answer_list = list(combinations(num_list, len(num_list) -k))
    return ''.join(max(answer_list))

def solution4(number, k):
    answer_list = list(combinations(number, len(number) -k))
    answer = ''
    for tmp_answer in answer_list :
        if answer == '' or answer < tmp_answer :
            answer = tmp_answer 
    return ''.join(answer)

def solution5(number, k):
    return ''.join(max(combinations(number, len(number) -k)))


print(solution_final(number, k ))