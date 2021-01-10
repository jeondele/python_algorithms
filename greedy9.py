# 프로그래머스 그리디 6번. 단속카메라(미결)

def solution(routes):
    answer = 0
    sorted_routes = sorted(routes, key = lambda x : [x[0], x[1]])
    visited = [False] * len(routes)
    for idx , route in enumerate(routes) :
        camera = 0 
        if visited[idx] == True :
            continue
        answer +=1
        visited[idx] = True
        camera = route[1] 
        for j in range(idx+1 , len(routes)) :
            if camera > routes[j][1] and routes[j][2] < camera :
                visited[j] = True
                camera = routes[j][2]
                
            
        
    return answer