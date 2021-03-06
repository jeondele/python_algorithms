#다이나믹 프로그래밍
#메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
#이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 합니다.
#다이나믹 구현 방식은 top-down , bottom-up 방식
#DP를 사용하는 조건 
#1. 최적의 부분구조 : 큰문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있을 때
#2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결할 때

#예시 1.피보나치
def fibo(x) :
  if x == 1 or x ==2 :
      return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(4))  


#단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 됨.
#같은 값을 여러번 호출하는 문제도 발견 됨.

#메모이제이션
#한번 계산한 결고ㅘ를 메모리 공간에 메모하는 기법
#값을 기록해 놓는다는 점에서 캐싱이라고도 함.


#예시 2. 메모이제이션을 활용한 피보나치
d = [0] *100

def fibo_m(x) :
  if x == 1 or x ==2 :
      return 1
  if d[x] != 0 :
      return d[x]

  d[x] = fibo(x-1) + fibo(x-2)        
  return d[x]

print(fibo_m(99))  


#예제 1. 개미전사
n = 4
input_val = [1, 3 , 1, 5]
dp = [0] * n
def ant(n, input_val) :
  if n == 0:
    return input_val[0]
  if n == 1:
    return max(input_val[0], input_val[1])
  dp[n] = max(ant(n-2, input_val) + input_val[n] , ant(n-1 , input_val))   
  return dp[n]

print(ant(n-1, input_val))

#최적의 풀이 
def ant(nput_val) :
  dp[0] = input_val[0]
  dp[1] = max(input_val[0], input_val[1])
  for i in range(2, n) :
    dp[i] = max(dp[i-1], dp[i-2] + input_val[i])   
  return dp[n]

print(dp[n-1])

#예제 2. 1로 만들기
d_1 = [0]* 30001
#bottom-up
for i in range(2, x+1) :
  d_1[i] = d_1[i-1] + 1
  if i % 2 == 0 :
    d_1[i] = min(d_1[i] , d_1[i//2] +1)
  if i % 3 == 0 :
    d_1[i] = min(d_1[i] , d_1[i//3] +1)   
  if i % 5 == 0 :
    d_1[i] = min(d_1[i] , d_1[i//5] +1)  
print(d[x])

#예제 3. 효율적인 화폐구성
n = 3
m = 7
array = [2, 3, 5]
d= [10001] * (m+1)
d[0] = 0
for i in range(n) :
  for j in range(array[i], m+1) :
    if(d[j - array[i] ] != 10001 :
      d[j] = min(d[j], d[j-array[i]] +1 )

if d[m] == 10001 :
  print(-1)
else :
  print(d[m])

#예제 4. 금광문제는 따로 풀어보기  

#예제 5. 병사 배치하기
#가장 긴 증가하는 부분 수열 LIS 로 알려진 다이나믹 프로그래밍
#D[i] = array[i]
#모든 원소 0 <= j < i에 대하여, D[i] = max(D[i] , D[j] +1) if array[j] < array[i]
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()
# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] *n 

for i in range(1,n) :
    for j in range(0, i) :
        if array[j] < array[i] :
            dp[i] = max(dp[i], dp[j]+1)
print(n- max(dp))            
