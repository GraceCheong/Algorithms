# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     now = 0
#     boxes = 0
#
#     for i in range(len(deliveries)) :
#         if deliveries[i] != 0 :
#             boxes += deliveries[i]
#             if boxes <= cap :
#                 now = i
#                 portable = cap
#                 deliveries[i] = 0
#                 for j in range(i):
#                     if (portable - pickups[i-j]) >= 0:
#                         portable -= pickups[i-j]
#                         pickups[i-j] = 0
#                     elif (portable - pickups[i-j]) < 0 :
#                         if portable == 0 :
#                             pickups[i-j] -= portable
#                         break
#
#         if i == len(deliveries)-1 and boxes > 0:
#             print(now)
#             answer += (now+1)*2
#             break
#
#         if boxes >= cap or (boxes + deliveries[i+1]) > cap:
#             print(now)
#             answer += (now+1)*2
#             boxes = 0
#
#     portable = cap
#     for j in range(len(pickups)):
#         portable -= pickups[j]
#         if pickups[j] != 0 :
#             now = j
#             if portable < 0 :
#                 portable += cap
#                 answer += (j+1)*2
#
#
#     print(deliveries)
#     print(pickups)
#     return answer