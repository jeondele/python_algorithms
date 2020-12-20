#정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요. 예를 들어 1을 입력했을 때 다음은 하나라도 3이 포함되어 있으므로 세어야 하는 시각입니다.
#1) 00시 00분 03초
#2) 00시 13분 30초

def imp () :
  N = int(input())
  none_3_case = 0
  case_3 = 0
  for num in range(1, N+1) :
    if '3' in str(num) :
      case_3 += 1

  none_3_case = (N+1) - case_3
  total_none_case = none_3_case * 5*9*5*9
  total_case = (N+1)*6*10*6*10

  return total_case - total_none_case

def brute_force_method() :
  N = int(input())
  cnt = 0
  for i in range(N +1) :
    for j in range(60) :
      for k in range(60) :
        if '3' in str(i) + str(j) + str(k) :
          cnt += 1
  return cnt

