def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        stack = []
        for s in skill_tree:
            if s in skill:
                stack.append(s)
        tmp = ''.join(stack)
        if tmp == skill[:len(tmp)]:
            answer += 1
    return answer
