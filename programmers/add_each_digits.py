def solution(n):
    answer = 0
    ls = [int(i) for i in list(str(n))]
    for i in ls:
        answer += i
    return answer
