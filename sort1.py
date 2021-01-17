#프로그래머스 정렬 1번. k번째 수

def solution(array, commands):
    answer = []
    for i in commands :
        answer.append(sorted(array[i[0]-1 : i[1]])[i[2]-1])
    return answer