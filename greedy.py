#그리디 알고리즘
#최소한의 아이디어로 해를 구하는 경우

#어떤 수 n이 1이 될때 까지 반복적으로 수행
#1.n에서 1을 뺀다
#2.n에서 k로 나눕니다.

#n이 1이 될때까지 수행하는 최소한의 횟수를 구하라

#나의 풀이
def greedy(n , k) :
  cnt = 0 
  while (n != 1)  :
    if n%k == 0 :
      n = n//k
      cnt += 1
    else : 
      n -= 1
      cnt += 1
  return cnt

#베스트 풀이 : O(n)에서 O(log(n))으로 수행가능
def improvedGreedy(n, k) :
  cnt = 0
  while True :
    #n이 k로 나누어 떨어지는 수가 될때까지 빼기
    target = (n//k) * k
    
    cnt += (n- target)
    n = target

    #n이 k보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출

    if n < k : 
      break
    
    #k로 나누기

    cnt += 1
    n //=k

  cnt += (n - 1)  
  return cnt