### 프로그래머스 3. 위장

#https://programmers.co.kr/learn/courses/30/lessons/42578

#### 나의 풀이

def solution(clothes):
    answer = 1
    dic_clothes = dict()
    
    for cloth in clothes :
        if cloth[1] in dic_clothes.keys() :
            dic_clothes[cloth[1]] +=1
        else :
            dic_clothes[cloth[1]] = 1
    
    for i in dic_clothes.values() :
        answer *= (i+1)
      
    return answer-1