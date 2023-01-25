import math

def solution(numbers):
    answer = []
    for item in numbers:
        temp = list((bin(item)[2:]))
        depth = math.ceil(math.log2(len(temp)))
        while len(temp) < 2 ** (math.ceil(math.log2(len(temp)))) - 1:
            temp.insert(0, '0')
        # depth 사용해서 풀이
        # print(temp)
        check = 0
        for i in range(1, depth+1):
            # d : 1 - log2(n) ex) if 17 : 1-4
            for k in range(math.ceil((len(temp)+1)// 2 ** (i+1))):
                mid = 2 ** i + 2 ** (i + 1) * k - 1
                l = mid - 2**(i-1)
                r = mid + 2**(i-1)
                # print(l+1,mid+1,r+1)
                # print(mid+1)
                if temp[mid] == '0' and (temp[l] == '1' or temp[r] == '1'):
                    #print("checked")
                    check += 1
            # if check > 0:
            #     answer.append(0)
                # break
        if check == 0 :
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([7, 42, 5]))
print(solution([63, 111, 95]))
print(solution([32767, 24575, 1056964543]))