from itertools import combinations

N, M, D = map(int, input().split())
enemy_list = []
maps = []
for r in range(N):
    arr = list(map(int, input().split()))
    for c in range(M):
        if arr[c]:
            enemy_list.append((r, c))
archers_list = [(N, i) for i in range(M)]
candidates = combinations(archers_list, 3)


# 각 궁수의 공격 범위
# 궁수의 저격 거리, 좌표값
def get_distance(candi):
    attack_ranges = []
    for pos in candi:
        attack_range = []
        for i in range(N):
            for j in range(M):
                dist = abs(pos[0] - i) + abs(pos[1] - j)
                if dist <= D:
                    attack_range.append((dist, i, j))
        attack_ranges.append(attack_range)
    return attack_ranges


# 적군이 전진
def go_to_castle(enemies):
    return set([(i + 1, j) for i, j in enemies if i < N - 1])


# 가장 가까운 적 선택
def choose_enemy(arc, enemies):
    arc.sort(key=lambda x: (x[0], x[2]))
    for d, i, j in arc:
        if (i, j) in enemies:
            return i, j
    return False


ans = 0
for archers in candidates:
    archers_range = get_distance(archers)
    terminates = 0
    enemy_set = set(enemy_list[:])
    while enemy_set:
        temp = set()
        for archer in archers_range:
            terminate = choose_enemy(archer, enemy_set)
            if terminate:
                temp.add(terminate)
        terminates += len(temp)
        enemy_set -= temp
        enemy_set = go_to_castle(enemy_set)

    if ans < terminates:
        ans = terminates

print(ans)
