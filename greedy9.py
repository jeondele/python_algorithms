# 프로그래머스 그리디 6번. 단속카메라(완료)

# 간단한 풀이..
def solution_best(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000
    answer = 0
    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]
    return answer
# 내풀이
def solution(routes):
    answer = 0
    sorted_routes = sorted(routes, key = lambda x : [x[0], x[1]])
    print(sorted_routes)
    visited = [False] * len(routes)
    for idx , route in enumerate(sorted_routes) :
        camera = 0 
        if visited[idx] == True :
            continue
        answer +=1
        visited[idx] = True
        camera = route[1] 
        for j in range(idx+1 , len(sorted_routes)) :
            if sorted_routes[j][0] <= camera and sorted_routes[j][1] <= camera :
                visited[j] = True
                camera = sorted_routes[j][1]
            if sorted_routes[j][0] <= camera and sorted_routes[j][1] >= camera :
                visited[j] = True
    return answer


print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2