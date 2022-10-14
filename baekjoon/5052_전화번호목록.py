import sys


# 1. Trie 자료구조 사용
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, s):
        cur_node = self.head
        for c in s:
            if c not in cur_node.children:
                cur_node.children[c] = Node(c)
            cur_node = cur_node.children[c]
        cur_node.data = s

    def search(self, s):
        cur_node = self.head
        for c in s:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
        if cur_node.children:
            return False
        else:
            return True


def determine(nums, trie):
    for num in nums:
        if not trie.search(num):
            return False
    return True


input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    trie = Trie()
    nums = []
    for _ in range(n):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)
    nums.sort()
    if determine(nums, trie):
        print('YES')
    else:
        print('NO')


# 2. 문자열 직접 비교
def check():
    for i in range(n - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            return False
    return True

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    nums.sort()
    if check():
        print('YES')
    else:
        print('NO')