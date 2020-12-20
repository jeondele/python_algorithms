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
    if int_x + dx[i] > 0 and int_y + dy[i] > 0 :
      #print(int_x +dx[i] , int_y + dy[i]  )
      cnt += 1
    if int_x + dx[i] > 0 and int_y - dy[i] > 0 :
      #print(int_x +dx[i] , int_y - dy[i]  )
      cnt += 1
    if int_x - dx[i]  > 0 and int_y + dy[i] > 0 :
      #print(int_x -dx[i] , int_y + dy[i]  )
      cnt += 1
    if int_x - dx[i] > 0 and int_y - dy[i] > 0 :
      #print(int_x -dx[i] , int_y - dy[i]  )  
      cnt += 1
  return cnt
