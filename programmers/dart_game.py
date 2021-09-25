def solution(dartResult):
    scores = []
    num = ''
    for i in dartResult:
        if i.isnumeric():
            num += i
            continue
        elif i.isalpha():
            if i == 'S':
                scores.append(int(num))
                num = ''
            elif i == 'D':
                scores.append(int(num) ** 2)
                num = ''
            elif i == 'T':
                scores.append(int(num) ** 3)
                num = ''
        elif i == '*':
            if len(scores) > 1:
                scores[-2] *= 2
            scores[-1] *= 2
        elif i == '#':
            scores[-1] *= -1

    return sum(scores)
