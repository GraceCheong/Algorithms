def solution(cap, n, deliveries, pickups):
    answer = 0
    now = 0
    portable = cap

    for i in range(len(deliveries)) :
        if deliveries[i] != 0 :
            portable -= deliveries[i]
            now = i

            if portable <= 0 :
                while(portable <= 0):
                    portable += cap
                    answer += (now+1)*2
                p = cap
                for j in range(i):
                    if (p - pickups[i-j]) >= 0:
                        p -= pickups[i-j]
                        pickups[i-j] = 0
                    elif (p - pickups[i-j]) < 0 :
                        if p == 0 :
                            pickups[i-j] -= p
                        break

            if i == len(deliveries)-1 and portable < cap:
                answer += (i+1)*2

    portable = cap
    for j in range(len(pickups)):
        portable -= pickups[j]
        if pickups[j] != 0 :
            now = j
            if portable < 0 :
                while(portable <= 0):
                    portable += cap
                    answer += (now+1)*2

    return answer

#
# 뭔가 실행하면 정상적으로 돌아가는데 테케 돌리면 1개 빼고 다 실패 뜸 : 뭔가 놓치고 있는 부분이 있다!