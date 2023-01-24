def solution(cap, n, deliveries, pickups):
    answer = 0
    deliverylist = []
    pickuplist = []

    for i in range(len(deliveries)):
        if deliveries[i] > 0:
            deliverylist.append((deliveries[i], i))
        if pickups[i] > 0:
            pickuplist.append((pickups[i], i))

    print(deliverylist, pickuplist)
    portable = cap

    while len(deliverylist) > 0 :
        weight, dist = deliverylist.pop(0)

        if weight <= portable :
            portable -= weight
            print(weight)
        else:
            while weight < portable:
                print(weight)
                print(dist+1)
                answer += (dist+1)*2
                weight -= cap
            portable -= weight

        if portable == 0 or len(deliverylist) == 0 :
            print(dist+1)
            answer += (dist+1)*2
            portable = cap

    return answer

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))