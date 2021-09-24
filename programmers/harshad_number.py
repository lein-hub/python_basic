def solution(x):
    sum_each = sum([int(x) for x in list(str(x))])

    if x % sum_each == 0:
        return True

    return False
