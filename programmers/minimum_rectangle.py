def solution(sizes):
    sorted_sizes = [sorted(i) for i in sizes]

    return max(i[0] for i in sorted_sizes) * max(i[1] for i in sorted_sizes)
