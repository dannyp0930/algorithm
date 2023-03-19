dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N = int(input())
room = [[0] * N for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N * N)]
for i in range(N * N):
    student = students[i]
    tmp = []
    for r in range(N):
        for c in range(N):
            if room[r][c] == 0:
                like = 0
                blank = 0
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if room[nr][nc] in student[1:]:
                            like += 1
                        elif room[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, r, c])
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    room[tmp[0][2]][tmp[0][3]] = student[0]

res = 0
students.sort()
for r in range(N):
    for c in range(N):
        like = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if room[nr][nc] in students[room[r][c] - 1]:
                    like += 1
        if like:
            res += 10 ** (like - 1)
print(res)
