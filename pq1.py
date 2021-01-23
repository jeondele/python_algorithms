#프로그래머스 우선순위큐 1번. 더 맵게

import heapq

def solution(scoville, K):
    heap =[]
    for num in scoville :
        heapq.heappush(heap, num)
    print(heap)
    answer = 0
    while heap[0] < K :
        try :
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
        except IndexError :
            return -1
        answer += 1
    return answer
