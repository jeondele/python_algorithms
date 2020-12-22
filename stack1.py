#프로그래머스 스택 1번. 주식가격 
#https://programmers.co.kr/learn/courses/30/lessons/42584

#효율성 0 풀이
def solution(prices):
  answer = []
  for idx, price in enumerate(prices) :
      if idx+1 == len(prices) :
          break
      for i , after_price in enumerate(prices[idx+1 : ]) :
          if i + 1 == len(prices[idx+1 : ]) :
              answer.append(i+1)
              break
          if price > after_price :
              answer.append(i + 1)
              break
  answer.append(0) 
  return answer

#그나마 나은 풀이
def solution2(prices):
  answer = [0] * len(prices)
  for idx in range(len(prices)) :
      if idx+1 == len(prices) :
          break
      for i in range(idx+1 , len(prices)) :
          if i + 1 == len(prices) :
              answer[idx] = len(prices) - idx - 1
              break
          if prices[idx] > prices[i] :
              answer[idx] = i-idx
              break      
  return answer




#list[0 : 8 : 2 ] 시작 : 끝 : 간격  
#창의적인 풀이
#대박풀이
def solution3(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans