melody = list(map(int, input().split()))
ascending = sorted(melody)
descending = sorted(melody, reverse=True)

if melody == ascending:
    print('ascending')
elif melody == descending:
    print('descending')
else:
    print('mixed')