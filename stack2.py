
#변수 i는 반복할 때마다 다음 값으로 덮어써지기 때문에 값을 할당해도 변수에 영향을 주지 못합니다.
#progresses = [95, 90, 99, 99, 80, 99]	
#speeds = 	[1, 1, 1, 1, 1, 1]
progresses = [93, 30, 55]
speeds = 	[1, 30, 5]

#첫번째풀이 일반적인 풀이
def solution(progresses, speeds):
    stack = []
    answer = []
    for progress , speed in zip(progresses , speeds) :
        x = (100 - progress) // speed 
        if (100 - progress) % speed > 0 :
            x +=1
        stack.append(x)
    print(''.join(str(stack)))
    loc = 0 
    for i in range(len(stack)) :
        if stack[loc] < stack[i]:
           answer.append(i - loc)
           loc = i
        if i == len(stack)-1 and stack[loc] >= stack[i] :
           answer.append(i - loc + 1)

              
    return answer

#두번째 풀이 스택
def solution2(progresses, speeds):
    stack = []
    answer = []
    for progress , speed in zip(progresses , speeds) :
        x = (100 - progress) // speed 
        if (100 - progress) % speed > 0 :
            x +=1
        stack.append(x)
    
    flag =True
    while (flag) :
      cnt = 0
      max_value = max(stack)
      target = stack.index(max_value)
      while (target <= len(stack) - 1) :
        stack.pop()
        cnt+=1
      answer.append(cnt)
      if not stack  :
        flag = False
    answer.reverse()    
    return answer


#세번째 베스트 풀이
def solution3(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            if (len(Q) > 0 ) :
              print(Q[-1][0])
              print(-((p-100)//s))
            Q.append([-((p-100)//s),1])
            print(''.join(str(Q)))
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

print(solution3(progresses, speeds))