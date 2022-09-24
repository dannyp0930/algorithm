string = input()
tmp = []
for i in range(1, len(string) - 1):
    for j in range(i + 1, len(string)):
        tmp.append(string[:i][::-1] + string[i:j][::-1] + string[j:][::-1])
tmp.sort()
print(tmp[0])