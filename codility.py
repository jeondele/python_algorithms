# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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