import sys


# 전위 순회
def pre_order(node):
    global result1
    result1 += node
    left, right = graph[node]["left"], graph[node]["right"]
    if left !='.':
        pre_order(left)
    if right != '.':
        pre_order(right)


# 중위 순회
def in_order(node):
    global result2
    left, right = graph[node]["left"], graph[node]["right"]
    if left !='.':
        in_order(left)
    result2 += node
    if right != '.':
        in_order(right)


# 후위 순회
def post_order(node):
    global result3
    left, right = graph[node]["left"], graph[node]["right"]
    if left !='.':
        post_order(left)
    if right != '.':
        post_order(right)
    result3 += node


input = sys.stdin.readline
N = int(input())
graph = dict()
for i in range(N):
    node, left, right = input().rstrip().split()
    graph[node] = { "left": left, "right": right}

result1 = ''
result2 = ''
result3 = ''

pre_order('A')
in_order('A')
post_order('A')

print(result1)
print(result2)
print(result3)
