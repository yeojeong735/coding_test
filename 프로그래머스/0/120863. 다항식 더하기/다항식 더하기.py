def solution(polynomial):
    answer = ''
    
    parts = polynomial.split(' + ')
    coef = 0
    const = 0
    
    for part in parts:
        if "x" in part:
            if part == "x":
                coef += 1
            else :
                part = part.replace("x", "")
                coef += int(part)
            
        else :
            const += int(part)
            
    if coef and const:  # 둘 다 있는 경우
        if coef == 1:
            return f"x + {const}"
        else:
            return f"{coef}x + {const}"
    elif coef:  # 계수만 있는 경우
        if coef == 1:
            return "x"
        else:
            return f"{coef}x"
    else:  # 상수만 있는 경우
        return str(const)
    

    return answer