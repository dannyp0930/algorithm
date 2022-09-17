dr = [0, 0, 1, -1, -1, -1, 1, 1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]

move_command = {
    'R': 0, 'L': 1, 'B': 2, 'T': 3,
    'RT': 4, 'LT': 5, 'RB': 6, 'LB': 7
}

def move(command):
    global kr, kc, sr, sc
    nkr = kr + dr[move_command[command]]
    nkc = kc + dc[move_command[command]]
    nsr, nsc = sr, sc
    if nkr < 0 or nkr > 7 or nkc < 0 or nkc > 7:
        return
    if nkr == sr and nkc == sc:
        nsr += dr[move_command[command]]
        nsc += dc[move_command[command]]
    if nsr < 0 or nsr > 7 or nsc < 0 or nsc > 7:
        return
    kr, kc = nkr, nkc
    sr, sc = nsr, nsc
    

k, s, N = map(str, input().split())
kr, kc = 8 - int(k[1]), ord(k[0]) - 65
sr, sc = 8 - int(s[1]), ord(s[0]) - 65
N = int(N)
for _ in range(N):
    command = input()
    move(command)
print(chr(kc + 65) + str(8 - kr))
print(chr(sc + 65) + str(8 - sr))
