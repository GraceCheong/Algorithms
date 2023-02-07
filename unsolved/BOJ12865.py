''' 
Problem: 평범한 배낭(12865)
BaekJoon Online
'''
def put(k, stack: list):
    if len(stack) <= 0 or k <= 0: 
        return 0
    s = stack.copy()

    w, v = s.pop()
    if len(s) == 0 :
        if w > k : 
            return 0 
    
    #print(w, v, s)

    if k-w < 0 : # cannot carry the item now
        return put(k, s)
    else : 
        res = max(put(k, s), v + put(k-w, s))
        del s 
        return res 

n, k = map(int, input().split())
stufflist = [tuple(map(int, input().split())) for i in range(n)]

print(put(k, stufflist))