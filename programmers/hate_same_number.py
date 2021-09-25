def solution(arr):
    result = [arr[0]]
    for i in arr[1:]:
        if result[len(result)-1] != i:
            result.append(i)

    return result
