def count(n):
    cnt, a, b = 0, n, 1
    while a:
        cnt += (n + 1) // (b << 1) * b
        if a & 1:
            cnt += (n + 1) % b
        a >>= 1
        b <<= 1
    return cnt

A, B = map(int, input().split())
print(count(B) - count(A - 1))
