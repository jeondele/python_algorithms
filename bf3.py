#프로그래머스 완전탐색 3번. 카펫
def solution(brown, yellow):
    answer = []
    x, y = 0, 0
    total = brown//2 + 2
    print(total)
    for i in range(total//2 , total - 2) :
        x , y = i , total - i
        if (x-2) * (y-2) == yellow :
            answer += sorted([x,y] , reverse = True)
            break
    return answer