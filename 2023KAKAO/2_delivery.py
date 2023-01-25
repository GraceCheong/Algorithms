def solution(cap, n, deliveries, pickups):
    answer = 0
    #youtube reference
    while deliveries or pickups :
        while deliveries and deliveries[-1] == 0:
            del deliveries[-1]
        while pickups and pickups[-1] == 0 :
            del pickups[-1]
        answer += 2 * max(len(deliveries), len(pickups))
        #until here
        cd, cp = cap, cap
        while cd > 0 and deliveries:
            if cd >= deliveries[-1] :
                cd -= deliveries[-1]
                del deliveries[-1]
            else:
                deliveries[-1] -= cd
                break
        while cp > 0 and pickups:
            if cp >= pickups[-1]:
                cp -= pickups[-1]
                del pickups[-1]
            else:
                pickups[-1] -= cp
                break
    return answer
