#8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요. 왕실의 정원에서 행 위치를 표현 할때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현합니다.

def night_location() :
  loc = ['a' ,'b', 'c', 'd', 'e', 'f', 'g', 'h']
  dx = [2,1]
  dy = [1,2]
  
  x , y   = map(str, input().split())

  int_x = int(loc.index(x))+1
  int_y = int(y)
  
  cnt = 0 
  for i in range(len(dx)) :
    if int_x + dx[i] >= 1 and int_x + dx[i] <= 8 and int_y + dy[i] >= 1 and int_y + dy[i] <= 8 :
      #print(int_x +dx[i] , int_y + dy[i]  )
      cnt += 1
    if int_x + dx[i] >= 1 and int_x + dx[i] <= 8 and int_y - dy[i] >= 1 and int_y - dy[i] <= 8:
      #print(int_x +dx[i] , int_y - dy[i]  )
      cnt += 1
    if int_x - dx[i] >= 1 and int_x - dx[i] <= 8 and int_y + dy[i] >= 1 and int_y + dy[i] <= 8 :
      #print(int_x -dx[i] , int_y + dy[i]  )
      cnt += 1
    if int_x - dx[i] >= 1 and int_x - dx[i] <= 8 and int_y - dy[i] >= 1 and int_y - dy[i] <= 8:
      #print(int_x -dx[i] , int_y - dy[i]  )  
      cnt += 1
  return cnt


#베스트 풀이 
#1.나이트가 이동할 수 있는 방향을 직접 다 정의
#2.알파벳을 아스키코드로 받아서 숫자로 표현

def best_night() :
  input_data = input()
  row = int(input_data[1])
  col = int(ord(input_data[0])) - int(ord('a')) + 1

  #나이트가 이동할 수 있는 8가지 방향 정의
  steps = [(-2, -1) , (-1, -2) , (1, -2) , (2, -1) , (2, 1), (1, 2), (-1, 2), (-2, 1)]

  #8가지 방향에 대하여 각 위치로 이동 가능한지 확인
  result = 0
  for step in steps :
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >=1 and next_row <= 8 and next_col >=1 and next_col <=8 :
      result += 1
  
  return result