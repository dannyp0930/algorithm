def f(x):
    if not x % 2:
        return x + 1
    else:
        n = (~x) & (x + 1)
        return (n | x) & ~(n >> 1)

def soultion(numbers):
    ans = []
    for num in numbers:
        ans.append(f(num))
    return ans

print(soultion([2, 7]))