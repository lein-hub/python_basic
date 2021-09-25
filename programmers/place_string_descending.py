def solution(s):
    ls = list(s)
    upper = []
    lower = []
    for i in ls:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)

    upper.sort(reverse=True)
    lower.sort(reverse=True)

    lower.extend(upper)

    return ''.join(lower)
