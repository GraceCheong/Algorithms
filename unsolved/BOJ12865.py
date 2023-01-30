''' 
Problem: 평범한 배낭(12865)
BaekJoon Online
'''
def put(k, max_val, sum_val, sum_weight, li:list, index, depth):
    depth += 1
    if sum_weight > k or index > len(li)-1 : 
        return max_val
    print(depth)
    nw, nv = li[index] # now value
    
    _max_val = max_val
    
    if sum_weight + nw <= k : 
        _max_val = max(_max_val, sum_val + nv, put(k, _max_val, sum_val + nv, sum_weight + nw, li, index+1, depth))

    for i in range(len(li)):
        _max_val = max(_max_val, 
                    put(k, _max_val, sum_val, sum_weight, li, index + i + 1, depth), # 없는 애들중 최고 
                    ) 

    return _max_val

n, k = map(int, input().split())
stufflist = [list(map(int, input().split())) for i in range(n)]

print(put(k, 0, 0, 0, stufflist, 0, 0))