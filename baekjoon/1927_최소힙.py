import sys

input = sys.stdin.readline

# 최소 힙 구현
def insert(num):
    # 단말 노드에 데이터 삽입
    heap.append(num)
    idx = len(heap) - 1
    # 부모 노드가 자신보다 크다면 위치 swap
    while idx != 1 and num < heap[idx // 2]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        idx //= 2

def delete():
    # 최소값 저장
    result = heap[1]
    # 마지막 노드와 루트 노드 값 swap
    heap[-1], heap[1] = heap[1], heap[-1]
    # 최소값 삭제
    heap.pop()

    parent = 1
    while 1:
        child = parent * 2
        if child + 1 < len(heap) and heap[child] > heap[child + 1]:
            child += 1
        if child >= len(heap) or heap[child] > heap[parent]:
            break
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
    print(result)



N = int(input())
heap = [0]
for _ in range(N):
    x = int(input())
    # x가 자연수인 경우
    if x:
        insert(x)
    # x가 0 인 경우
    else:
        # heap에 값이 존재하면
        if len(heap) > 1:
            delete()
        # heap에 값이 존재하지 않는다면
        else:
            print(0)

# heapq 사용
import heapq

heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    # x가 자연수인 경우
    if x:
        heapq.heappush(heap, x)
    # x가 0 인 경우
    else:
        # heap에 값이 존재하면
        if heap:
            print(heapq.heappop(heap))
        # heap에 값이 존재하지 않는다면
        else:
            print(0)