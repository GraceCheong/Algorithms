def solution(n, m, x, y, r, c, k):
    li = []
    answer = ''

    # 프로그래머스 김도원님 코드 참고
    diff = abs(r-x) + abs(c-y)
    # 예외처리 먼저 : 출발지점과 도착지점 사이의 칸수 차이가 움직임 횟수보다 크거나 홀짝수가 안맞으면 pass
    if diff%2!=k%2 or diff>k:
        return 'impossible'

    #dlru 순서로 가기
    #왜냐면 어차피 맨 앞에꺼만 구하면되기 때문에
    dcount = 0
    lcount = 0
    rcount = 0
    ucount = 0

    if x < r :
        dcount = r-x
    else :
        ucount = x-r
    if c < y :
        lcount = y-c
    else :
        rcount = c-y

    rest = k - diff

    xplus = min(n-max(x,r), rest//2)
    rest -= xplus * 2
    yplus = min(min(y, c)-1, rest//2)
    rest -= yplus*2

    answer = 'd'*(dcount+xplus)+'l'*(lcount+yplus)+'rl'*(rest//2)+'r'*(rcount+yplus)+'u'*(xplus+ucount)
    return answer
