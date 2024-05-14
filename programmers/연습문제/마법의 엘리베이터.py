def solution(storey):
    ans = 0
    while storey:
        re = storey % 10
        if re == 5:
            if storey % 100 // 10 >= 5:
                storey += 10
            ans += 5
        elif re > 5:
            ans += 10 - re
            storey += 10
        else:
            ans += re
        storey //= 10
    return ans