def solution(dirs):
    answer = 0
    d = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    visit = [[{'U': 0, 'D': 0, 'R': 0, 'L': 0} for _ in range(11)] for _ in range(11)]
    r, c = 5, 5
    for dir in dirs:
        nr, nc = r + d[dir][0], c + d[dir][1]
        re_dir = ''
        if dir == 'U':
            re_dir = 'D'
        elif dir == 'D':
            re_dir = 'U'
        elif dir == 'R':
            re_dir = 'L'
        else:
            re_dir = 'R'
        if 0 <= nr <= 10 and 0 <= nc <= 10:
            if not visit[nr][nc][re_dir]:
                answer += 1
                visit[r][c][dir] = 1
                visit[nr][nc][re_dir] = 1
            r, c = nr, nc
    return answer