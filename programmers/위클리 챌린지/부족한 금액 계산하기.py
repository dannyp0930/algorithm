def solution(price, money, count):
    total = 0
    for i in range(1, count + 1):
        total += i * price
    if total > money:
        return total - money
    return 0
