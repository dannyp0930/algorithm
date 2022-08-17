class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node["*"] = s
    
    def print(self, level, cur_node):
        if '*' in cur_node: return
        cur_child = sorted(cur_node)
        for c in cur_child:
            print('--' * level + c)
            self.print(level + 1, cur_node[c])


N = int(input())
ans = Trie()
for _ in range(N):
    tmp = list(input().split())
    ans.insert(tmp[1:])
ans.print(0, ans.root)