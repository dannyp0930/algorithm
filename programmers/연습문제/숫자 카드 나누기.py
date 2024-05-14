def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        n = a % b
        a, b = b, n
    return a


def getGcd(arr):
    cur = arr[0]
    for i in range(1, len(arr)):
        if cur == 1:
            return cur
        cur = gcd(cur, arr[i])
    return cur


def canDivide(mod, arr):
    for n in arr:
        if not n % mod:
            return True
    return False


def solution(arrayA, arrayB):
    ans = 0
    n = len(arrayA)
    a = getGcd(arrayA)
    b = getGcd(arrayB)
    if not canDivide(a, arrayB):
        ans = max(ans, a)
    if not canDivide(b, arrayA):
        ans = max(ans, b)
    return ans
