import math

def dfs (temp:list, i:int, depth):
    if depth < 1 :
        return 1

    l = int(i - 2 ** (depth-1))
    r = int(i + 2 ** (depth-1))

    if temp[i-1] == '0':
        if temp[l-1] == '1' or temp[r-1] == '1':
            return 0

    return dfs(temp, l, depth - 1) * dfs(temp, r, depth - 1)

def solution(numbers):
    answer = []
    for item in numbers:
        temp = list(bin(item)[2:])
        depth = math.ceil(math.log2(len(temp)))

        while len(temp) < 2 ** depth - 1:
            temp.insert(0, '0')

        answer.append(dfs(temp, (len(temp)+1) // 2, depth - 1))
    return answer


# 예외처리가 틀린건 없음
# 나중에 오답하고 우선 dfs 로 방식 변경해서 구현 해도 똑같다.
#
# math 가 문제일까?



#
# def solution(numbers):
#     answer = []
#     for item in numbers:
#         temp = list(bin(item)[2:])
#         depth = math.ceil(math.log2(len(temp)))
#         while len(temp) < (2 ** depth - 1):
#             temp.insert(0, '0')
#         check = 0
#         for k in range(1, depth):
#             for i in range((len(temp)+1) // 2 ** (k+1)):
#                 mid = 2 **k + 2 ** (k+1) * i
#                 if temp[mid-1] == '0':
#                     if temp[mid - 2 **(k-1) - 1] == '1' or temp[mid + 2 ** (k - 1) - 1] == '1':
#                         check += 1
#         del temp
#         if check > 0:
#             answer.append(0)
#         else:
#             answer.append(1)
#     return answer

print(solution([7, 42, 5]))
print(solution([63, 111, 95, 165150075007]))


# 합계: 10.0 / 100.0 맞는거 같은데 ㅡㅡ 화가난다.. 일단 오늘은 여기까지