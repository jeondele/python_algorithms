# 프로그래머스 5번. 섬 연결하기(미결)
# kruskal 알고리즘을 활용해야 풀수있을듯.. 미결상태
n = 4	
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 5
costs = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]
#n = 5
#costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]] 
#answer = 7
#n = 4
#costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]
#return 9
n=6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
#답 11
def bfs(start, node, costs , visited):
    #print(start[0])
    queue =[start]
    visited[costs.index(start)] = True
    while queue :
        next_val = queue.pop(0)
        if node[next_val[1]] == 0 or node[next_val[1]] >  next_val[2] :
            node[next_val[1]] = next_val[2]
        if node[next_val[0]] == 0  :
            node[next_val[0]] = next_val[2]    
        print(node)
        for idx , cost in enumerate(costs) :
            if visited[idx] == True :
                continue
            if next_val[0] == cost[0] or next_val[1] == cost[0] or next_val[0] == cost[1] or next_val[1] == cost[1]  :
                print(cost)
                queue.append(cost)
                visited[idx] = True
    print(node)
    print(visited)
    return sum(node) - node[start[0]]
def solution(n, costs):
    node = [0] * n
    visited = [False] * len(costs)
    sorted_costs = sorted(costs, key = lambda x : [x[2], x[0], x[1]], reverse = False)
    print(sorted_costs)
    return bfs (sorted_costs[0], node, sorted_costs , visited)

def solution2(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합]
    print(routes)
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans
print(solution2(n, costs))