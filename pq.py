#우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
#스택 : 가장 나중에 삽입된 데이터 
#큐 : 가장 먼저 삽입된 데이터
#우선순위 큐 : 가장 우선순위가 높은 데이터
#단순히 리스트를 이용하여 구현 -- 삽입시간 O(1) 삭제시간(O(N))
#힙(heap)을 이용하여 구현가능-- 삽입시간 O(logN) 삭제시간(O(logN))
#힙 : 오ㅘㄴ전 이진 트리 자ㅏ료구조ㅗ
# 힙에서는 항상 루트 노드를 제거한다
#최소 힙 == 값이 작은 데이터가 우선적으로 제거
#최대 힙 == 값이 큰 데이터가 우선적으로 제거
#완전 이진트리 : 루트부터 시작하여 왼쪽 노드, 오른쪽 노드 순서대로 데이터가 들어감
#Min-Heapify()
#힙에서 원소가 제거될때 가장 높은 노드의 값으로 대체

import sys
import heapq
input = sys.stdin.readline

def hehapsort(iterable) :
    h = []
    result = []
    for value in iterable :
        heapq.heappush(h, value)
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr= []

for i in range(n) :
    arr.append(int(input()))
res = heapsort(arr)
for i in range(n) :
    print(res[i])