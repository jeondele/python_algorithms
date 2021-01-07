#프로그래머스 그리디 4번. 섬 연결하기 
#bfs 생각중..
def bfs(start, costs , visited):
    visited[start] = True
    queue = [start]
    while queue and False in visited :
        start = queue.pop(0)
        for step in costs :
            if step[0] == start and visited[step[1]] == False :
                queue.append(step[1])
                visited[step[1]] = True

def solution(n, costs):
    visited = [False] * n
    answer = 0
    sorted_costs = sorted(costs, key = lambda x : [costs[2], costs[0], costs[1]], reverse = False)
                    
    for step in costs[0] :
        bfs
    return answer