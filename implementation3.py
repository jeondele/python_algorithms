#알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파멧을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
#예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.


def sort_word() :
  mixed = input()
  alphabet_list = []
  num_list = 0

  for i in mixed :
    if ord(i) < 65 :
      num_list += int(i)
    else :
      alphabet_list.append(i)

  alphabet_list.sort()
  
  string = ''
  for alphabet in alphabet_list :
    string += alphabet
  
  if num_list != 0 :
    string += str(num_list)
  return string

#베스트 풀이

def best_sort_word() :
  data = input()
  result = []
  value = 0

  for x in data :
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha() :
      result.append(x)
    else :
      value += int(x)
  result.sort()

  #숫자가 하나라도 존재하는 경우에만 뒤에 삽입
  if value != 0 :
    result.append(str(value))
  
  #최종 결과를 for문 돌려서 출력할 때는 ''.join 을 사용하면 간결하다
  return ''.join(result)