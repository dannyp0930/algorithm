import sys


def insert(x):
    abs_x = abs(x)
    heap.append((abs_x, x))
    idx = len(heap) - 1
    while idx != 1 and abs_x <= heap[idx // 2][0]:
        if abs_x == heap[idx // 2][0] and x > heap[idx // 2][1]:
            break
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        idx //= 2


def remove():
    min_x = heap[1]
    heap[-1], heap[1] = heap[1], heap[-1]
    heap.pop()

    parent = 1
    size = len(heap)
    while 1:
        child = parent * 2
        # 자식 노드가 없는 경우
        if child + 1> size:
            break
        # 자식 노드가 한 개인 경우
        elif child + 1 == size:
            # 자식 노드의 절댓값이 더 큰 경우
            if heap[child][0] > heap[parent][0]:
                break
            # 자식 노드와 절댓값이 같고 자식노드의 값이 더 큰 경우 
            elif heap[child][0] == heap[parent][1] and heap[child][1] > heap[parent][1]:
                break
        # 자식 노드가 두 개인 경우
        else:
            left_child_abs, left_child = heap[child]
            right_child_abs, right_child = heap[child + 1]
            parent_abs, parent_x = heap[parent]
            # 자식 노드들의 절댓값이 큰 경우
            if left_child_abs > parent_abs and right_child_abs > parent_abs:
                break
            # 왼쪽 자식 노드의 절댓값이 같고 값이 더 큰 경우
            elif left_child_abs == parent_abs and left_child > parent_x and right_child_abs > parent_abs:
                break
            # 오른쪽 자식 노드의 절댓값이 같고 값이 더 큰 경우
            elif left_child_abs > parent_abs and right_child_abs == parent_abs and right_child > parent_x:
                break
            else:
                # 오른쪽 자식 노드의 절댓값이 작은 경우
                if left_child_abs > right_child_abs:
                    child += 1
                # 자식 노드들의 절댓값이 같고 오른쪽 자식 노드의 값이 작은 경우
                elif left_child_abs == right_child_abs and left_child > right_child:
                    child += 1
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
    return min_x[1]

input = sys.stdin.readline
N = int(input())
heap = [(0, 0)]
for _ in range(N):
    x = int(input())
    if x == 0:
        # 힙이 비어있는 경우
        if len(heap) == 1:
            print(0)
        else:
            print(remove())
    else:
        insert(x)
