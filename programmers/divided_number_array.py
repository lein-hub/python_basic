def solution(arr, divisor):
    result = []
    for i in arr:
        if i % divisor == 0:
            result.append(i)

    return sorted(result) if len(result) else [-1]
