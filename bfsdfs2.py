#프로그래머스 2번. 네트워크
#단순이 그래프의 연결을 따지는 게 아니라 , 해당 네트워크들 간의 이동 까지 고려해야하는 문제

def dfs(computers, visited, v):
    if visited[v] == 0:
        visited[v] = 1
    for e in range(len(computers)):
        print("e ::: " , e )
        if computers[v][e] == 1 and visited[e] == 0:
            dfs2(computers, visited, e)

def solution(n, computers):
    visited = [0] * n
    ans = 0
    while 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                print("i ::: " ,  i)
                dfs2(computers, visited, i)
                ans += 1
    return ans