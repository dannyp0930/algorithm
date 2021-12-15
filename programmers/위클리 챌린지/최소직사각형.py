def solution(sizes):
    width = height = 0
    for size in sizes:
        width = max(width, max(size))
        height = max(height, min(size))
    return width * height
