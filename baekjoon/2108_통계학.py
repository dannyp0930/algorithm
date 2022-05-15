N = int(input())
arr = []
total = 0
count = [0] * 8001
max_cnt = 0

# 전체 합 및 카운팅
for _ in range(N):
    num = int(input())
    total += num
    count[num + 4000] += 1

for i in range(8001):
    if count[i]:
        # 카운팅 정렬
        for _ in range(count[i]):
            arr.append(i - 4000)
        # 최빈도 찾기
        if max_cnt < count[i]:
            max_cnt = count[i]

# 최빈값 넣기
modes = []
for j in range(8001):
    if count[j] == max_cnt:
        modes.append(j - 4000)

# 산술평균
print(round(total / N))

# 중앙값
print(arr[N // 2])

# 최빈값
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# 범위
print(arr[- 1] - arr[0])
