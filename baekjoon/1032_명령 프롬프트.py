N = int(input())
ans = list(input())
for _ in range(N - 1):
    string = input()
    for i in range(len(ans)):
        if ans[i] != string[i]:
            ans[i] = '?'
print(''.join(ans))
