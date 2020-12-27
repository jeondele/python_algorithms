numbers = [1, 1, 1, 1, 1]	
target = 3

#nonlocal 함수를 써서 선언된 함수 밖 변수에 값을 저장할 수 있다.
def solution(numbers, target):
    n = len(numbers)
    cnt = 0
    def dfs(L, total):
        if L == n:
            if total == target:
                nonlocal cnt
                cnt += 1
        else:
            dfs(L+1, total+numbers[L])
            dfs(L+1, total-numbers[L])
    
    dfs(0,0)
    return cnt

#깔끔하고 간단한 코드.. 왜생각을 못하지..
def solution2(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


from itertools import product
l = [(1, -1), (1, -1), (1, -1), (1, -1), (1, -1)]
print(list(product(*l)))

# * 가변인자를 받을 때 사용
# product 곱집합 나타낼 때 사용
# [(1, -1), (1, -1), (1, -1), (1, -1), (1, -1)] 의 각 튜플 별 원소들끼리 합의 경우의 수를 나타냄
# count : 리스트 안의 target의 갯수를 셈
def solution3(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
print(solution3(numbers, target))