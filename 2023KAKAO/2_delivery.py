def pickup(cap, location, pickups:list):
    temp, templist = cap, pickups.copy()
    # pickup 새로 구현하기 여기서 문제 생긴듯?

def deliver(cap, stack, deliveries:list, pickups:list, result):
    weight, location = deliveries[0]
    #print(f"weight : {weight}, location : {location} ", end= "")

    if weight > stack[0] :
        # if weight > stack , then fix weight to stack, remain the item in de deliveries
        deliveries[0][0] = weight - stack[0]
        stack[0] = cap
        #print("stack:", stack[0])
        # goto pickup
        # print(deliveries)
        pickup(cap, location, pickups)
        # print((location + 1) * 2)
        return (location + 1) * 2
    elif weight == stack[0] :
        # if weight equal to stack , renew the stack to cap and weight == 0 delete the delivered item
        stack[0] = cap
        deliveries.pop(0)
        #print("stack:", stack[0])
        # goto pickup
        pickup(cap, location, pickups)
        # print(deliveries)
        # print((location + 1) * 2)
        return (location + 1) * 2
    else :
        # if weight is less then stack, stack = stack - weight, delete the delivered item
        stack[0] = stack[0] - weight
        deliveries.pop(0)
        # print(deliveries)
        #print("stack:", stack[0])
        # go next
        if len(deliveries) < 1:
            return result + (location + 1) * 2
        return deliver(cap, stack, deliveries, pickups, result)


def solution(cap, n, deliveries, pickups):
    answer = 0
    _deliveries = []
    stack = [cap]

    for i in range(0, n):
        if deliveries[i] > 0:
            _deliveries.append([deliveries[i], i]) # add delivery item to deliverylist ex) (weight, location)
        if pickups[i] > 0:
            pickups.append([pickups[i], i])  # add delivery item to deliverylist ex) (weight, location)
    #print(_deliveries)
    while len(_deliveries) > 0 :
        answer += deliver(cap, stack, _deliveries, pickups, 0)
    while len(pickups) > 0 :

    return answer

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))

## 하나 더 맞음.. 뭐가 문제일까 ㅠㅅ ㅠ