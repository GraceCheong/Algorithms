def solution(numbers):
    answer = []
    for item in numbers:
        temp = list(reversed(bin(item)[2:]))
        check = 0

        for i in range(len(temp) // 2):
            if temp[i * 2 + 1] != '1':
                if temp[i*2] == '1' or temp[i*2 +2] == '1':
                    check += 1
                    answer.append(0)
                    break
        del temp

        if check > 0:
            answer.append(0)
        else:
            answer.append(1)
    return answer

print(solution([7, 42, 5]))
print(solution([63, 111, 95]))

print(solution([88888, 453453, 444444444444444555]))

# 합계: 40.0 / 100.0