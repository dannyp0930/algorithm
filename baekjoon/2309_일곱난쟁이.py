# 백트래킹

def dwarf():
    for i in range(9):
        for j in range(i + 1, 9):
            if arr[i] + arr[j] == tot - 100:
                for k in range(9):
                    if k == i or k == j:
                        continue
                    print(arr[k])
                return


arr = [int(input()) for _ in range(9)]
arr.sort()
tot = 0
for num in arr:
    tot += num
dwarf()
