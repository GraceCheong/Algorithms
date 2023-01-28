def find_road(n, m, Nx, Ny, Ex, Ey, k, count, li:list, way:str):
    if count == k :
        if Nx == Ex and Ny == Ey :
            li.append(way)
        return
    else :
        #able to go up
        if Nx > 1 :
            find_road(n, m, Nx-1, Ny, Ex, Ey, k, count+1, li, way+"u")
        #able to go down
        if Nx < n :
            find_road(n, m, Nx+1, Ny, Ex, Ey, k, count+1, li, way+"d")
        #able to go right
        if Ny < m :
            find_road(n, m, Nx, Ny+1, Ex, Ey, k, count+1, li, way+"r")
        #able to go left
        if Ny > 1 :
            find_road(n, m, Nx, Ny-1, Ex, Ey, k, count+1, li, way+"l")
        return

def solution(n, m, x, y, r, c, k):
    li = []
    answer = ''

    find_road(n, m, x, y, r, c, k, 0, li, "")

    if len(li) > 0:
        _min = "z"
        for item in li :
            if _min > item:
                _min = item
        answer = _min
    else :
        answer = "impossible"

    return answer
