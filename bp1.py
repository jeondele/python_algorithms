#프로그래머스 완전탐색 1.모의고사
def solution(answers):
    answer = []
    no_1 = [1,2,3,4,5]
    no_2 = [2,1,2,3,2,4,2,5]
    no_3 = [3,3,1,1,2,2,4,4,5,5]
    c1 = 0
    c2 = 0
    c3 = 0
    for idx , no in enumerate(answers) :
        if no == no_1[idx % len(no_1)] :
            c1 += 1
        if no == no_2[idx % len(no_2)] :
            c2 += 1
        if no == no_3[idx % len(no_3)] :
            c3 += 1
    if max(c1, c2, c3 ) == c1 :
        answer.append(1)
    if max(c1, c2, c3 ) == c2 :
        answer.append(2)
    if max(c1, c2, c3 ) == c3 :
        answer.append(3)   
    return answer