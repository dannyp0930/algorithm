N = int(input())
arr = list(map(int, input().split()))
count = [0] * N
for i in range(N - 1):
    for j in range(i + 1, N):
        # 기울기 m
        m = (arr[j] -arr[i]) / (j - i)
        # y절편 n
        n = arr[i] - m * i

        # i, j를 잇는 직선을 지나거나 접하는 직선이 없다면 두 빌딩은 서로 보인다.
        for k in range(i + 1, j):
            if m * k + n <= arr[k]:
                break
        else:
            count[i] += 1
            count[j] += 1
print(max(count))
