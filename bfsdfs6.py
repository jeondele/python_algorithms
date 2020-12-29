# 프로그래머스 dfsbfs 4번. 여행경로

#tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
tickets = [['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]
#e답 : [ICN, B, ICN, A]
answer = []

def func(x) :
    if x[0] == 'ICN' :
      return ( str(0) , x[1])
    else :
      return (x[0], x[1])

def dfs(city , tickets , visited) :
    if False not in visited :
        return True
    for i, ticket in enumerate( tickets ) :
        if visited[i] == False and city == ticket[0] :
            visited[i] = True
            answer.append(ticket[1])
            flag = dfs(ticket[1], tickets , visited)
            if flag == False :
                visited[i] = False
                answer.pop()
                continue
            return True
    return False

    

def solution(tickets):
    global answer 
    sorted_tickets = sorted(tickets , key = lambda x: func(x), reverse = False)
    visited = [False]* len(tickets)
    answer.append('ICN')
    dfs('ICN', sorted_tickets , visited)
    return answer

print(solution(tickets))