# def solution(rows, columns, queries):
#     answer = []
#     arr = [[i + 1 + j * rows for i in range(columns)] for j in range(rows)]
#     for lst in arr:
#         print(lst)
#     return answer

rows = 4
columns = 3
arr = [[i + 1 + j * columns for i in range(columns)] for j in range(rows)]

for lst in arr:
    print(lst)