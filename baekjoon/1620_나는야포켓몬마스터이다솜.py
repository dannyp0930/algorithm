import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pokedex_key = {i: input().rstrip() for i in range(1, N + 1)}
pokedex_value = {v: k for k, v in pokedex_key.items()}
for _ in range(M):
    quiz = input().rstrip()
    if quiz.isdigit():
        print(pokedex_key[int(quiz)])
    else:
        print(pokedex_value[quiz])
