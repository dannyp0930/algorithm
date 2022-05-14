words = set()
for _ in range(int(input())):
    words.add(input())
words = list(words)
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)
