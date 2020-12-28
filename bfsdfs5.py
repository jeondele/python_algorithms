#프로그래머스 dfsbfs 3번. 단어변환
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

answer = 0

#dfs풀이
def dfs(begin,target,words,visited):
    global answer
    stacks = [begin]
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer
        
        for word in words :
            cnt = 0
            for i , w in zip(stack , word) :
                if i != w :
                  cnt += 1
            if cnt == 1:
              if visited[words.index(word)] != 0:
                  continue
              visited[words.index(word)] = 1
              stacks.append(word)
        answer +=1

#bfs풀이
def bfs(begin , target , words, visited) :
    q = [begin]
    while q :
      next_val = q.pop(0)
      if next_val == target :
          return visited[words.index(next_val)]

      for word in words :
          cnt = 0
          if visited[words.index(word)] != 0 :
              continue
          for v , w in zip(next_val , word) :
              if v != w :
                  cnt +=1
          if cnt == 1 :
              if next_val not in words :
                  visited[words.index(word)] = 1
              else :
                  visited[words.index(word)] = visited[words.index(next_val)] + 1  
              q.append(word)
    return visited[words.index(target)]

def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    visited = [0] * len(words)
    #visited_flag = [False] * len(words)
    #dfs(begin,target,words,visited)

    #return answer 
    return bfs(begin,target,words,visited)

print(solution(begin, target, words))