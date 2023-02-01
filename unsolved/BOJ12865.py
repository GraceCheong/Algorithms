''' 
Problem: 평범한 배낭(12865)
BaekJoon Online
'''
def put(k, stack: list):
    if len(stack) <= 0 or k <= 0: 
        return 0
    s = stack.copy()

    w, v = s.pop()
    if not s :
        if w > k : 
            return 0 
    
    res = max(put(k, s), (v + put(k-w, s)) if k-w >=0 else 0)
    #print(k, w, v, s, res)
    del stack 
    return res 

n, k = map(int, input().split())
stufflist = [list(map(int, input().split())) for i in range(n)]

print(put(k, stufflist))