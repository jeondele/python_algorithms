#프로그래머스 그리디 1번. 체육복
#n	lost	reserve	return
#5	[2, 4]	[1, 3, 5]	5
#5	[2, 4]	[3]	4
n = 3	
lost = [3]	
reserve = [1]
#그리디에 맞지 않는 풀이..
def solution(n, lost, reserve):
    new_lost = []
    for l in lost :
        if l in reserve :
            reserve.pop(reserve.index(l))
            continue
        if l-1 not in new_lost :
            new_lost.append(l -1 )
        if l+1 not in new_lost :
            new_lost.append(l +1 )
    save = 0
    while (reserve) :
        if reserve.pop(0) in new_lost :
            save += 1
    
    return min (n , n - len(lost) + save)

print(solution(n, lost, reserve))

def solution(n, lost, reserve):
    visited = [False] * len(lost)
    save = 0
    for l in lost :
        if l in reserve :
            reserve.pop(reserve.index(l))
            visited[lost.index(l)] = True
    for l in lost :
        if visited[lost.index(l)] == True :
            continue
        if l-1 in reserve :
            reserve.pop(reserve.index(l-1))
            save += 1
            continue
        if l+1 in reserve  :
            reserve.pop(reserve.index(l+1))
            save += 1
            continue
    
    return n - len(lost) + save + visited.count(True)
    