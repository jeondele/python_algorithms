### 프로그래머스 4. 베스트앨범

#https://programmers.co.kr/learn/courses/30/lessons/42579

#### 나의 풀이
genres=["classic","classic","classic","classic","pop"]
plays=[500,150,800,800,2500]

def solution(genres, plays):
    answer = []
    hash_genres = dict()
    total_dic = dict()
    for i, genre in enumerate(genres) :
        if genre in hash_genres.keys() :
            hash_genres[genre].append((i , plays[i]))
            total_dic[genre]  +=  plays[i]
        else :
            hash_genres[genre] = [(i , plays[i])]
            total_dic[genre]  =  plays[i]
    
    sorted_total_dic = sorted(total_dic.items() , key = lambda x : (x[1], x[0]) , reverse = True)
    print(total_dic.items())
    total_dic = sorted(total_dic.items() , key = lambda x : (x[1], x[0]) , reverse = True)
    
    print(sorted_total_dic)
    print(total_dic)
    for list_in in sorted_total_dic :
        
        hash_genres[list_in[0]] = sorted(hash_genres[list_in[0]] , key = lambda x : (x[1], -x[0]) , reverse = True)
        
        answer.append(hash_genres[list_in[0]][0][0])
        if len(hash_genres[list_in[0]]) >=2 :
            answer.append(hash_genres[list_in[0]][1][0])
        
    return answer