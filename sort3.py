#프로그래머스 정렬 3번. H-Index
def solution_best(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
def solution(citations):
    answer = 0
    citations = sorted(citations , reverse = True)
    for i in range(len(citations)) :
        if i+1 >= len(citations)-i-1 :
            if citations[i] >= answer :
                answer = min(i+1 , citations[i])
    return answer