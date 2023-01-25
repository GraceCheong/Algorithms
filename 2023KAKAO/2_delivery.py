def pickup(cap, location, pickups:list):
    start, end = 0, -1
    distance = 0
    temp = cap
    # pickup 새로 구현하기 여기서 문제 생긴듯?
    if len(pickups) < 1 : return 0
    for i in range(len(pickups)-1, -1, -1):
        weight, loc = pickups[i]
        if temp <= 0: return distance
        if loc <= location and pickups[i][0] > 0:
            if temp == cap: distance, end = (loc + 1) * 2, i
            if weight >= temp :
                pickups[i][0] -= temp
                start = i
                break
            else:
                temp -= weight
                pickups[i][0] = 0
    return distance


def deliver(cap, stack, deliveries:list, pickups:list, result):
    weight, location = deliveries[0]
    #print(f"weight : {weight}, location : {location} ", end= "")

    if weight > stack[0] :
        # if weight > stack , then fix weight to stack, remain the item in de deliveries
        deliveries[0][0] -= stack[0]
        stack[0] = cap
        # goto pickup
        pickup(cap, location, pickups)
        return (location + 1) * 2
    elif weight == stack[0] :
        # if weight equal to stack , renew the stack to cap and weight == 0 delete the delivered item
        stack[0] = cap
        deliveries.pop(0)
        # goto pickup
        pickup(cap, location, pickups)
        return (location + 1) * 2
    else :
        # if weight is less then stack, stack = stack - weight, delete the delivered item
        stack[0] = stack[0] - weight
        deliveries.pop(0)
        # print(deliveries)
        #print("stack:", stack[0])
        # go next
        if len(deliveries) < 1:
            pickup(cap, location, pickups)
            return result + (location + 1) * 2
        return deliver(cap, stack, deliveries, pickups, result)


def solution(cap, n, deliveries, pickups):
    answer = 0
    _deliveries = []
    _pickups = []
    stack = [cap]

    for i in range(0, n):
        if deliveries[i] > 0:
            _deliveries.append([deliveries[i], i]) # add delivery item to deliverylist ex) (weight, location)
        if pickups[i] > 0:
            _pickups.append([pickups[i], i])  # add delivery item to deliverylist ex) (weight, location)

    while len(_deliveries) > 0 :
        answer += deliver(cap, stack, _deliveries, _pickups, 0)

    while len(_pickups) > 0 :
        if _pickups[-1][0] == 0 :
            _pickups.pop(-1)
            continue
        answer += pickup(cap, n, _pickups)
    return answer

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))

## 하나 더 맞음.. 뭐가 문제일까 ㅠㅅ ㅠ