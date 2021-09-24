import math


def solution(n):
    m = math.sqrt(n)
    if m % 1 == 0:
        return math.pow(int(m)+1, 2)
    return -1
