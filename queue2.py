# max함수에 리스트 객체의 길이가 0 이면 런타임 에러
# 리스트 객체의 빈 리스트는 None 값이 False 임... 빈리스트 인지 비교는 len()으로 해야함
def solution(priorities, location):
    idx_list = [i for i in range(len(priorities))]
    answer = 0
    while (location in idx_list) :
        pop_value = priorities.pop(0)
        pop_idx = idx_list.pop(0)
        if len(priorities) > 0 and pop_value < max(priorities) :
            priorities.append(pop_value)
            idx_list.append(pop_idx)
        else :
            answer += 1
    return answer