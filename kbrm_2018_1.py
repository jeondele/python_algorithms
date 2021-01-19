#카카오 2018 신입공채 1차 다트게임
import re

#정규표현식
#\d+ => 숫자가 한개이상 존재해야한다
#[SDT] => S D T 중에 하나가 존재해야한다
#[*#]? => * # 둘 중 하나가 있어도 되고 없어도 된다.
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    print(p)
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*':
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    print(dart)
    answer = sum(dart)
    return answer
print(solution('1D2S#10S'))


def solution(dartResult):
    z = ['S', 'D', 'T']
    o = ['*', '#']
    n = ['1','2','3','4','5','6','7','8','9','0']
    num = 0
    num_list = []
    e_10 = False
    for i in range(len(dartResult)) :
        if dartResult[i] in n :
            if dartResult[i] == '1' and dartResult[i+1] == '0' :
                e_10 = True
                continue
            if e_10 ==  False:
                if dartResult[i+1] == 'S' :
                    num = int(dartResult[i]) ** 1
                if dartResult[i+1] == 'D' :
                    num = int(dartResult[i]) ** 2
                if dartResult[i+1] == 'T' :
                    num = int(dartResult[i]) ** 3
            else :
                if dartResult[i+1] == 'S' :
                    num = 10 ** 1
                if dartResult[i+1] == 'D' :
                    num = 10 ** 2
                if dartResult[i+1] == 'T' :
                    num = 10 ** 3
                e_10 = False
            num_list.append(num)
            continue
        if dartResult[i] in z :
            if i == len(dartResult) -1 :
                break
            if dartResult[i+1] in n :
                continue
            if dartResult[i+1] in o :
                if dartResult[i+1] == '*' :
                    print(num_list)
                    idx = len(num_list)-1
                    while idx >= 0 :
                        if (len(num_list)-1) - idx >= 2:
                            break
                        num_list[idx] = num_list[idx] * 2
                        idx -= 1
                    continue
                if dartResult[i+1] == '#' :
                    num_list[-1] = num_list[-1] * (-1)
                    continue
        if dartResult[i] in o :
            if i == len(dartResult) -1 :
                break
    print(num_list)
    return sum(num_list)