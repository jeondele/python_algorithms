#프로그래머스 정렬 2번. 가장 큰 수
#ceil 할때는 math 임포트해야함
import math
def solution(numbers):
    def func(x) :
        return (str(x) * math.ceil(4 / len(str(x))))[0:5]
    return str(int(''.join(list(map(str, sorted(numbers , key = lambda x : func(x) , reverse = True ))))))

def solution_best(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))