import sys
input = sys.stdin.readline


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


for _ in range(int(input())):
    h, w = map(int, input().split())
    arr = ['.' * (w + 2)] + ['.' + input().rstrip() + '.' for _ in range(h)] + ['.' * (w + 2)]
    key = input().rstrip()
    keys = [0] * 26
    if key != '0':
        for k in key:
            keys[ord(k) - 97] = 1
    visit = [[0] * (w + 2) for _ in range(h + 2)]
    ans = 0
    q = [(0, 0)]
    doors = [[] for _ in range(26)]
    visit[0][0] = 1
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < h + 2 and 0 <= nc < w + 2:
                if arr[nr][nc] == '*': continue
                if not visit[nr][nc]:
                    visit[nr][nc] = 1
                    if arr[nr][nc] == '$': ans += 1
                    elif 'A' <= arr[nr][nc] <= 'Z':
                        d = ord(arr[nr][nc]) - 65
                        if not keys[d]:
                            doors[d].append((nr, nc))
                            continue
                    elif 'a' <= arr[nr][nc] <= 'z':
                        k = ord(arr[nr][nc]) - 97
                        keys[k] = 1
                        while doors[k]:
                            kr, kc = doors[k].pop(0)
                            q.append((kr, kc))
                    q.append((nr, nc))
    print(ans)