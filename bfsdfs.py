#재귀함수는 stack과 같다.
#최대공약수 계산 (유클리드 호제법) 예제
#유연하게 생각하기
def GCD(a, b) :
  if a % b == 0 :
    return b
  return GCD(b, a%b)

#dfs : 깊이 우선 탐색
#1.탐색 시작 노드를 스택에 삽입하고 방문처리 한다
#2.스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다.
#3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

visited = [False] * 9

def dfs(graph , v , visited) :
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v] :
    if not visited[i] :
      dfs(graph , i , visited)

#bfs : 우선너비 탐색
#그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
#큐 자료구조를 이용
#탐색 시작 노드를 큐에 삽입하고 방문처리를 합니다.
#큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리합니다.
#더이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
from collections import deque
def bfs (graph , v, visited) :
  queue = deque([v])
  visited[v] = True
  while queue :
    p = queue.popleft()
    print(p , end = ' ')
    for i in graph[p] :
      if not visited[i] :
        queue.append(i)
        visited[i] = True