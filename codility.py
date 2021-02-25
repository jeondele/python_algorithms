# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solutionMaxCounters(N, A):
    list_a = [0] * N
    cnt = 0 
    for idx , i in enumerate(A) :
        if i <= N : 
            break
        if idx == len(A)-1 :
            return list_a
    for i in A :
        if i > N : 
            list_a = [cnt] * N
        else :
            list_a[i-1] += 1
            if list_a[i-1] > cnt :
                cnt = list_a[i-1] 
    return list_a 
    
def solutionFrogRiverOne(X, A):
    if X > len(A) :
        return -1 
    flag = [False] * (X+1)
    flag[0] = True
    sx = (X * (X+1)) / 2
    for idx , i in enumerate(A) :
        if flag[i] == False :
            flag[i] = True
            sx -= i
            # 배열에서 False가 있는지 체크하면 그만큼 연산 소요가 많이됨
            #if idx >= (X-1) and False not in flag :
            if sx == 0 :
                return idx      
    return -1

def solutionTapeEquilibrium(A):
    #sum을 연산하면 O(n) 만큼 사용
    #리슷트의 길이가 10만 이상일때는 O(N^2)이니 조심
    arr = []
    sum_init = 0 
    sum_a = sum(A)
    for i in range(len(A)-1) :
        sum_init = sum_init + A[i]
        gap = sum_a - sum_init
        diff = abs(sum_init - gap)
        if diff == 0 :
            return 0
        arr.append(diff)
    return min(arr) 
 
def solutionPermMissingElem(A):
    flag = ['False'] * (len(A) + 2)
    for i in A :
        flag[i] = 'True'
    for idx, i in enumerate(flag) :
        if idx > 0 and i == 'False' :
            return idx 
    return None 

import math
def solutionFrogJmp(X, Y, D):
    if Y- X <= 0 :
        return 0
    return math.ceil((Y-X)/D) 



def solutionOddOccurrencesInArray(A):
    dict_a = {}
    for i in A :
        if i not in dict_a.keys() :
            dict_a[i] = 1
        else :
            dict_a[i] += 1

    for i in dict_a.keys() :
        if dict_a[i] % 2 > 0 :
            return i 
    return None
    
def solutionCyclicRotation(A, K):
    lens = len(A)
    if lens == 0 :
        return A 
    
    K = K%lens 
    return A[lens - K : ] + A[ : lens- K]


def solutionBinaryGap(N):
    #print(format(N , 'b')) #1111 -> 15
    #print(type(format(N , 'b'))) # str
    bin_n = format(N , 'b')
    print(bin_n)
    max = 0 
    cnt = 0
    for idx, i in enumerate(bin_n) :
        if i == '1' :
            if cnt > max :
                max = cnt
            cnt = 0
            continue
        cnt += 1
    return max


#print(solution(1376796946))