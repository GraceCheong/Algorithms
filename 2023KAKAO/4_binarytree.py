import math

def dfs (temp:list, i:int, depth):
    if depth == 0 :
        return 1

    if temp[i] == '0':
        if temp[i - depth] == '1' or temp[i + depth] == '1':
            return 0

    print(i - depth, i, i + depth)

    l = dfs(temp, i - depth, depth // 2)
    r = dfs(temp, i + depth, depth // 2)

    return l * r

def solution(numbers):
    answer = []
    for item in numbers:
        temp = bin(item)[2:]
        d = len(bin(len(temp))[2:]) # math 사용하지 않고 len과 bin 활용하는게 핵심!

        while len(temp) < 2 ** d:
            temp = '0' + temp

        i = len(temp) // 2
        # print(c)

        print(d, temp, i, i // 2)
        answer.append(dfs(temp, i, i//2))
        del temp
    return answer



# print(bin(7) + bin(1))

#
print(solution([7, 42, 5]))
# print(solution([63, 111, 95, 165150075007]))


# 합계: 10.0 / 100.0 맞는거 같은데 ㅡㅡ 화가난다.. 일단 오늘은 여기까지