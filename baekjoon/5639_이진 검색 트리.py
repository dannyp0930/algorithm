import sys

def postorder(s, e):
    if s > e:
        return
    root = preorder[s]
    m = e + 1
    for i in range(s + 1, e + 1):
        if root < preorder[i]:
            m = i
            break
    postorder(s + 1, m - 1)
    postorder(m, e)
    print(root)


input = sys.stdin.readline
preorder = []
while 1:
    try:
        n = int(input())
        preorder.append(n)
    except:
        break
postorder(0, len(preorder) - 1)