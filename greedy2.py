#각 자리가 숫자 (0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 
#왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫사 사이에 
#'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질수 있는 
#가장 큰 수를 구하는 프로그램을 작성하세요

#int 형으로 설정할 경우 약 21억 까지 가능
#파이썬은 큰 문제 없음

#나의 풀이
def maxOutput(input_value) :
  output = 0
  for num in input_value :
    if output + num < output * num :
      output *= num
    else :
      output += num
  return output

#best 풀이

def improvedMaxOutput(input_value) :
  result = 0
  for num in input_value :
    #두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    if num <=1 or result <= 1 :
      result += num
    else :
      result *= num
  return result