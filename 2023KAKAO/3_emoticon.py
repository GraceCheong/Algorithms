def to4(num, res:list, j):
    if j < 0:
        return

    q, r = divmod(num, 4)
    res[j] += r * 0.1
    #res[j] = (1-res[j]) * emoticons[j]
    if r == 2 :
        res[j] = 0.3
    elif r == 5:
        res[j] = 0.6
    if q >= 0:
        to4(q, res, j-1)

def solution(users, emoticons):
    answer = []
    cases = [[0.1]*len(emoticons) for i in range(pow(4, len(emoticons)))]
    for i in range(len(cases)):
        to4(i, cases[i], len(emoticons)-1)
    _max = [0, 0]
    for case in cases:
        _buying = 0
        _emo = 0
        for p, l in users :
            b = 0
            for i in range(len(case)):
                b += int(case[i] >= (p / 100)) * (1-case[i]) * emoticons[i]
            _emo += int(b >= l)
            _buying += int(b < l) * b
            # print(_emo, b, l, _buying)
        #print(_emo, _buying, _max)
        if _emo > _max[0] :
            _max[0]= _emo
            _max[1] = _buying
            #print(_buying, _emo)
        elif _emo == _max[0]:
            if _buying > _max[1]:
                _max[1] = _buying
                #print(_buying, _emo)

    #print(cases)
    return _max

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))