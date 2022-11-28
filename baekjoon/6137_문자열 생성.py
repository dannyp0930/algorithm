N = int(input())
S = [input() for _ in range(N)]
T = []
s, e = 0, N - 1
while s <= e:
    if S[s] < S[e]:
        T.append(S[s])
        s += 1
    elif S[s] > S[e]:
        T.append(S[e])
        e -= 1
    else:
        l, r = s, e
        while l <= r:
            if S[l] < S[r]:
                T.append(S[s])
                s += 1
                break
            elif S[l] > S[r]:
                T.append(S[e])
                e -= 1
                break
            else:
                l += 1
                r -= 1
        else:
            T.append(S[s])
            s += 1
cnt = 0
for ch in T:
    print(ch, end='')
    cnt += 1
    if cnt % 80 == 0:
        print()
