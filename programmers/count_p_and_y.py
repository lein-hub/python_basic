def solution(s):
    s = list(s.lower())
    p = s.count('p')
    y = s.count('y')

    return p == y
