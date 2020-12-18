### 프로그래머스 2. 전화번호 목록

#https://programmers.co.kr/learn/courses/30/lessons/42577

#나의 풀이
phoneBook = ["119", "97674223", "1195524421"]
phoneBook = ['12','123','1235','567','88']

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        for j in phone_book[i+1:]:
            if phone_book[i] in j:
                return False
    return True