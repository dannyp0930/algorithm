N, M = map(int, input().split())
arr = [input() for _ in range(N)]
ans = ''
cnt = 0
for i in range(M):
    DNA = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(N):
        DNA[arr[j][i]] += 1
    dna = ''
    tmp = 0
    for k, v in DNA.items():
        if v > tmp:
            dna, tmp = k, v
    ans += dna
    cnt += (N - tmp)
print(ans)
print(cnt)
