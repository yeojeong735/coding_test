def solution(dots):
    
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]
    
    def parallel(xa, ya, xb, yb, xc, yc, xd, yd):
        return (yb - ya) * (xd - xc) == (yd - yc) * (xb - xa)
    
    if parallel(x1, y1, x2, y2, x3, y3, x4, y4):
        return 1
    if parallel(x1, y1, x3, y3, x2, y2, x4, y4):
        return 1
    if parallel(x1, y1, x4, y4, x2, y2, x3, y3):
        return 1
    
    return 0